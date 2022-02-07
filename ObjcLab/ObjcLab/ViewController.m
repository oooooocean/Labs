//
//  ViewController.m
//  ObjcLab
//
//  Created by qiangchen on 2022/1/26.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSMutableDictionary *map = @{
        @"a": @1,
        @"b": @2,
        @"c": @3
    };
    
    for (int i = 0; i < 3; i++) {
        NSLog(@"--> %d", i);
        map[map.allKeys[0]] = nil;
    }
}


@end
