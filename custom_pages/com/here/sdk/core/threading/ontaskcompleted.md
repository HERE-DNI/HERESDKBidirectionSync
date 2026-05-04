---
title: "OnTaskCompleted (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestontaskcompleted"
hidden: false
---

Package [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface OnTaskCompleted

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface OnTaskCompleted
The method will be called on the main thread when a task call has been completed.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTaskCompleted](#onTaskCompleted(com.here.sdk.core.threading.TaskOutcome))`(`[`TaskOutcome`](sdk-for-android-explore-api-reference-latesttaskoutcome "enum class in com.here.sdk.core.threading")` taskOutcome)`

The method will be called on the main thread when a task call has been completed.

## Method Details

### onTaskCompleted

void onTaskCompleted(@NonNull [TaskOutcome](sdk-for-android-explore-api-reference-latesttaskoutcome "enum class in com.here.sdk.core.threading") taskOutcome)

    The method will be called on the main thread when a task call has been completed.
Parameters:
    `taskOutcome` -

    The task outcome
