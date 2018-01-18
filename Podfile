platform :ios, '9.0'

use_frameworks!

def common_dependencies
    pod 'RxSwift'
end

def test_dependencies
    pod 'Nimble'
end

def not_really_dependencies
    pod 'SwiftGen'
end

target 'ios-starter' do
    common_dependencies
    not_really_dependencies
end

target 'ios-starterTests' do
    test_dependencies
end
