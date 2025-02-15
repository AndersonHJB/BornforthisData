/*
 * @Time    : 2024/12/18 09:18
 * @Author  : AI悦创
 * @FileName: PrivateExample.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package com.example;

public class PrivateExample {
    private String privateField = "I am private!";

    private void privateMethod() {
        System.out.println("This is a private method.");
    }

    public void accessPrivate() {
        System.out.println("Accessing privateField: " + privateField);
        privateMethod();
    }
}
