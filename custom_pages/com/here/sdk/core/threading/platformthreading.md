---
title: "PlatformThreading (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplatformthreading"
hidden: false
---

Package [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface PlatformThreading

------------------------------------------------------------------------
public interface PlatformThreading
Interface for task activities on the main thread.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [postToMainThread](#postToMainThread(com.here.sdk.core.threading.Runnable))`(`[`Runnable`](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading")` runnable)`

Posts task to the end of the queue of the main thread.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [postToMainThread](#postToMainThread(com.here.sdk.core.threading.Runnable,long))`(`[`Runnable`](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading")` runnable, long delayMs)`

Posts a task to be executed on the main thread after some delay.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [runOnMainThread](#runOnMainThread(com.here.sdk.core.threading.Runnable))`(`[`Runnable`](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading")` runnable)`

Runs a task on the main thread.

## Method Details

### runOnMainThread

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") runOnMainThread(@NonNull [Runnable](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading") runnable)

    Runs a task on the main thread. If this function is called from the main thread, then the task will run immediately. Otherwise, it is put to the end of the queue of the main thread. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.
Parameters:
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of runnable is unknown.

    Returns:
    Handle that will be used to manipulate execution of the task.

### postToMainThread

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") postToMainThread(@NonNull [Runnable](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading") runnable, long delayMs)

    Posts a task to be executed on the main thread after some delay. If the delay is 0, the function puts the task at the end of the queue. The function does not wait for the task to be executed and returns immediately after the task has been put in the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.
Parameters:
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of runnable is unknown.

    `delayMs` -

    Delay in milliseconds.

    Returns:
    Handle that will be used to manipulate execution of the task.

### postToMainThread

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") postToMainThread(@NonNull [Runnable](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading") runnable)

    Posts task to the end of the queue of the main thread. Function does not wait for task to be executed and returns immediately after the task is put to the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.
Parameters:
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of runnable is unknown.

    Returns:
    Handle that will be used to manipulate execution of the task.
