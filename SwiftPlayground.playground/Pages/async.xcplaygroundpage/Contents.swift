import UIKit
import SwiftUI
import Foundation
import PlaygroundSupport

/// 异步函数：提供语法工具，使用更简洁和高效的方式，表达异步行为。
/// 结构化并发：提供并发的运行环境，负责正确的函数调度、取消和执行顺序以及任务的生命周期。
/// actor 模型：提供封装良好的数据隔离，确保并发代码的安全。

let images = ["https://pic.3gbizhi.com/2021/0923/20210923104742858.jpg",
              "https://pic.3gbizhi.com/2021/0923/20210923104742925.jpg",
              "https://pic.3gbizhi.com/2021/0923/20210923104743863.jpg",
              "https://pic.3gbizhi.com/2021/0923/20210923104743739.jpg",
              "https://pic.3gbizhi.com/2021/0923/20210923104744158.jpg"]

/// await 则代表了函数在此处可能会放弃当前线程, 它是程序的潜在暂停点.
/// 语句将被底层机制分配到其他合适的线程, 在执行完成后, 之前的“暂停”将结束, 异步方法从刚才的 await 语句后开始, 继续向下执行.
func asyncLoadImage(_ url: String) async -> UIImage {
    let (data, _ ) = try! await URLSession.shared.data(from: URL(string: url)!)
    return UIImage(data: data)!
}

/// 结构化并发
/// 1. 一个任务具有它自己的优先级和取消标识, 它可以拥有若干个子任务并在其中执行异步函数.
/// 2. 当一个父任务被取消时, 这个父任务的取消标识将被设置, 并向下传递到所有的子任务中去.
/// 3. 无论是正常完成还是抛出错误, 子任务会将结果向上报告给父任务, 在所有子任务完成之前 (不论是正常结束还是抛出), 父任务是不会完成的.
///
/// 上下文:
/// 在调用异步函数时, 需要在它前面添加 await 关键字;
/// 而另一方面, 只有在异步函数中, 我们才能使用 await 关键字.  第一个异步函数执行的上下文, 或者说任务树的根节点, 是怎么来的？
/// Task: 构建异步任务执行的上下文.
///
/// 方式一:
/// async let 被称为异步绑定, 它在当前 Task 上下文中创建新的子任务,
/// 并将它用作被绑定的异步函数的运行环境.
/// 和 Task.init 新建一个任务根节点不同, async let 所创建的子任务是任务树上的叶子节点.
/// 被异步绑定的操作会立即开始执行, 即使在 await 之前执行就已经完成, 其结果依然可以等到 await 语句时再进行求值.
///
/// 方式二:
/// Task group: withThrowingTaskGroup, withTaskGroup
func loadAllImage(_ urls: [String]) async -> [UIImage] {
    await withTaskGroup(of: UIImage.self, body: { group in
        for url in urls {
            group.addTask(priority: .none) {
                await asyncLoadImage(url)
            }
        }
        var results = [UIImage]()
        for await result in group {
            results.append(result)
        }
        return results
    })
}

/// 线程安全
/// 方式一:
/// 将相关的代码放入一个串行的 dispatch queue 中, 然后以同步的方式把对资源的访问派发到队列中去执行.
/// 方式二:
/// NSLock 或者 NSRecursiveLock
/// 方式三: actor 模型
/// 可以认为 actor 就是一个“封装了私有队列”的 class
/// actor 内部会提供一个隔离域: 在 actor 内部对自身存储属性或其他方法的访问, 可以不加任何限制, 这些代码都会被自动隔离在被封装的“私有队列”里.
/// 但是从外部对 actor 的成员进行访问时, 编译器会要求切换到 actor 的隔离, 以确保数据安全.
/// 在这个要求发生时, 当前执行的程序可能会发生暂停. 编译器将自动把要跨隔离域的函数转换为异步函数, 并要求我们使用 await 来进行调用.

class AsyncUIObject: ObservableObject {
    @Published var results: [UIImage] = []
    
    func load() {
        Task {
            results.append(contentsOf: await loadAllImage(images))
            objectWillChange.send()
        }
    }
}

struct AsyncView: View {
    @ObservedObject var object = AsyncUIObject()
    
    var body: some View {
        VStack {
            Button("开始加载") {
                object.load()
            }
            
            ScrollView {
                ForEach(object.results, id: \.self) { image in
                    Image(uiImage: image)
                        .resizable()
                        .scaledToFit()
                }
            }
        }
        .frame(width: 300, height: 700, alignment: .center)
    }
}

PlaygroundPage.current.liveView = {
    return UIHostingController(rootView: AsyncView())
}()
