/*
 * @Time    : 2024/12/15 18:58
 * @Author  : AI悦创
 * @FileName: ProtectedClass.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package com.example;

// 这是一个受保护的类，只能在同一个包中或子类中访问
public class ProtectedClass {
    // 受保护字段
    protected String protectedField = "I am protected!";

    // 受保护方法
    protected void protectedMethod() {
        System.out.println("This is a protected method.");
    }
}
