---
title: "LogAppender (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlogappender"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface LogAppender

------------------------------------------------------------------------
public interface LogAppender
An interface to implement a listener to receive log messages.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [log](#log(com.here.sdk.core.engine.LogLevel,java.lang.String))`(`[`LogLevel`](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")` level, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` message)`

## Method Details

### log

void log(@NonNull [LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine") level, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Parameters:
    `level` -

    The severity of the log message.

    `message` -

    The log message.
