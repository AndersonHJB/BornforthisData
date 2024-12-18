/*
 * @Time    : 2024/12/15 18:51
 * @Author  : AI悦创
 * @FileName: MainTest.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package com.example;

import com.example.subpackage.SubClass;

public class MainTest {
    public static void main(String[] args) {
        // 创建 PublicClass 的实例
        PublicClass publicClass = new PublicClass();

        // 访问 publicField
        System.out.println("Accessing publicField: " + publicClass.publicField);

        // 调用 publicMethod
        publicClass.publicMethod();


        // 在 MainTest 中测试 ProtectedClass
        // 测试 ProtectedClass
        ProtectedClass protectedClass = new ProtectedClass();

        // 在同一个包内，访问受保护字段和方法
        System.out.println("Accessing protectedField: " + protectedClass.protectedField);
        protectedClass.protectedMethod();

        // 在 MainTest 中测试 SubClass
        SubClass subClass = new SubClass();
        subClass.testProtectedAccess();

        // 在 MainTest 中测试 DefaultClass
        DefaultClass defaultClass = new DefaultClass();
        System.out.println(defaultClass.defaultField);
        defaultClass.defaultMethod();

        // 在 MainTest 中测试 PrivateExample
        PrivateExample privateExample = new PrivateExample();
        // System.out.println(privateExample.privateField);  // 会报错
        privateExample.accessPrivate();




    }
}
