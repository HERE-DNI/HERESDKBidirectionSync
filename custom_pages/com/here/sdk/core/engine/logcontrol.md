---
title: "LogControl (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlogcontrol"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LogControl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.LogControl
------------------------------------------------------------------------
public final class LogControl extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK. Note, this class will load native libraries of SDK, therefore generally it should be used just before SDK initialization, otherwise, it might have an unexpected performance impact if called not at the right time.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [LogControl.InvalidPathException](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception)

Invalid file path exception.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static void`

  [disableLoggingToConsole](#disableLoggingToConsole())`()`

Disables SDK logging messages to console.

`static void`

  [enableLoggingToConsole](#enableLoggingToConsole(com.here.sdk.core.engine.LogLevel))`(`[`LogLevel`](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")` level)`

Enables SDK logging messages to console that can be viewed using logcat tool.

`static void`

  [removeAppender](#removeAppender())`()`

Removes previously added custom log appender.

`static void`

  [setAppender](#setAppender(com.here.sdk.core.engine.LogLevel,com.here.sdk.core.engine.LogAppender))`(`[`LogLevel`](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")` level, `[`LogAppender`](sdk-for-android-explore-api-reference-latestlogappender "interface in com.here.sdk.core.engine")` appender)`

Sets a custom log appender to receive log messages from the SDK.

`static void`

  [setAppender](#setAppender(com.here.sdk.core.engine.LogLevel,java.lang.String))`(`[`LogLevel`](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")` level, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` path)`

Sets a custom log appender that will write SDK log messages to a file.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### enableLoggingToConsole

public static void enableLoggingToConsole(@NonNull [LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine") level)

    Enables SDK logging messages to console that can be viewed using logcat tool. Enabled by default with [`LogLevel.LOG_LEVEL_INFO`](sdk-for-android-explore-api-reference-latestloglevel#LOG_LEVEL_INFO).
Parameters:
    `level` -

    Log level.

### disableLoggingToConsole

public static void disableLoggingToConsole()

    Disables SDK logging messages to console. Enabled by default with [`LogLevel.LOG_LEVEL_INFO`](sdk-for-android-explore-api-reference-latestloglevel#LOG_LEVEL_INFO).

### setAppender

public static void setAppender(@NonNull [LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine") level, @NonNull [LogAppender](sdk-for-android-explore-api-reference-latestlogappender "interface in com.here.sdk.core.engine") appender)

    Sets a custom log appender to receive log messages from the SDK. This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use [`disableLoggingToConsole()`](#disableLoggingToConsole()) API.
Parameters:
    `level` -

    Log level.

    `appender` -

    New log appender.

### setAppender

public static void setAppender(@NonNull [LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine") level, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) path) throws [LogControl.InvalidPathException](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception "class in com.here.sdk.core.engine")

    Sets a custom log appender that will write SDK log messages to a file. This overwrites a previous custom log appender set by user. Note, that setting the custom appender does not disable logging to the console made by SDK, in order to do that use [`disableLoggingToConsole()`](#disableLoggingToConsole()) API.
Parameters:
    `level` -

    Log level.

    `path` -

    Absolute path to a file that the application has read/write permissions.

    Throws:
    [`LogControl.InvalidPathException`](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception "class in com.here.sdk.core.engine") -

    [`LogControl.InvalidPathException`](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception "class in com.here.sdk.core.engine") Indicates that the file path is invalid or not writeable.

### removeAppender

public static void removeAppender()

    Removes previously added custom log appender.
