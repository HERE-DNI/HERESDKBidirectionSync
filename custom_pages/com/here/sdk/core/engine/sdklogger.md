---
title: "SDKLogger (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdklogger"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SDKLogger

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.SDKLogger
------------------------------------------------------------------------
public final class SDKLogger extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Logging interface for Android/iOS platforms. These logs are under management of [`LogControl`](sdk-for-android-explore-api-reference-latestlogcontrol "class in com.here.sdk.core.engine") and should be used instead of platform-specific logging functions.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static void`

  [error](#error(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` tag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

convenient function to print a message with log level ERROR and tag.

`static void`

  [fatal](#fatal(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` tag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

convenient function to print a message with log level FATAL and tag.

`static void`

  [info](#info(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` tag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

convenient function to print a message with log level INFO and tag.

`static void`

  [log](#log(com.here.sdk.core.engine.LogLevel,java.lang.String,java.lang.String))`(`[`LogLevel`](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")` level, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` tag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

  `static void`

  [warn](#warn(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` tag, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

convenient function to print a message with log level WARNING and tag.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### log

public static void log(@NonNull [LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine") level, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Parameters:
    `level` -

    The severity of the log message.

    `tag` -

    The log tag.

    `message` -

    The log message.

### info

public static void info(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)

    convenient function to print a message with log level INFO and tag.
Parameters:
    `tag` -

    The log tag.

    `message` -

    The log message.

### warn

public static void warn(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)

    convenient function to print a message with log level WARNING and tag.
Parameters:
    `tag` -

    The log tag.

    `message` -

    The log message.

### error

public static void error(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)

    convenient function to print a message with log level ERROR and tag.
Parameters:
    `tag` -

    The log tag.

    `message` -

    The log message.

### fatal

public static void fatal(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) tag, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)

    convenient function to print a message with log level FATAL and tag.
Parameters:
    `tag` -

    The log tag.

    `message` -

    The log message.
