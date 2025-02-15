/*
 * @Time    : 2024/12/18 08:58
 * @Author  : AI悦创
 * @FileName: SubClass.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package com.example.subpackage;

import com.example.ProtectedClass;

// SubClass 继承 ProtectedClass
public class SubClass extends ProtectedClass {
    public void testProtectedAccess() {
        // 访问受保护的成员
        System.out.println("Accessing protectedField: " + protectedField);
        protectedMethod();
    }
}
