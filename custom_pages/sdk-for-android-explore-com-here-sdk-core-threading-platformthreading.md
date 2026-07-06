---
title: "PlatformThreading (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-threading-platformthreading"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">PlatformThreading</span>

</div>

<div class="block">

Interface for task activities on the main thread.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      postToMainThread(Runnable runnable)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Posts task to the end of the queue of the main thread.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      postToMainThread(Runnable runnable,
       long delayMs)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Posts a task to be executed on the main thread after some delay.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      runOnMainThread(Runnable runnable)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Runs a task on the main thread.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-runOnMainThread(com.here.sdk.core.threading.Runnable)"
    class="section detail">

    ### runOnMainThread

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">runOnMainThread</span><span class="parameters">(@NonNull
    [Runnable](sdk-for-android-explore-com-here-sdk-core-threading-runnable "interface in com.here.sdk.core.threading") runnable)</span>

    </div>

    <div class="block">

    Runs a task on the main thread. If this function is called from the
    main thread, then the task will run immediately. Otherwise, it is
    put to the end of the queue of the main thread. Note: Depending on
    actual platform, destruction-time of passed in runnable might be
    unknown due to unpredictability of garbage collection. Therefore,
    runnable should not hold strong references to objects whose
    lifetimes are critical or references should be released at the end
    of execution.

    </div>

    Parameters:  
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of
    runnable is unknown.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>
<div id="sdk-for-android-explore-postToMainThread(com.here.sdk.core.threading.Runnable,long)"
    class="section detail">

    ### postToMainThread

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">postToMainThread</span><span class="parameters">(@NonNull
    [Runnable](sdk-for-android-explore-com-here-sdk-core-threading-runnable "interface in com.here.sdk.core.threading") runnable,
    long delayMs)</span>

    </div>

    <div class="block">

    Posts a task to be executed on the main thread after some delay. If
    the delay is 0, the function puts the task at the end of the queue.
    The function does not wait for the task to be executed and returns
    immediately after the task has been put in the queue. Note:
    Depending on actual platform, destruction-time of passed in runnable
    might be unknown due to unpredictability of garbage collection.
    Therefore, runnable should not hold strong references to objects
    whose lifetimes are critical or references should be released at the
    end of execution.

    </div>

    Parameters:  
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of
    runnable is unknown.

    `delayMs` -

    Delay in milliseconds.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>
<div id="sdk-for-android-explore-postToMainThread(com.here.sdk.core.threading.Runnable)"
    class="section detail">

    ### postToMainThread

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">postToMainThread</span><span class="parameters">(@NonNull
    [Runnable](sdk-for-android-explore-com-here-sdk-core-threading-runnable "interface in com.here.sdk.core.threading") runnable)</span>

    </div>

    <div class="block">

    Posts task to the end of the queue of the main thread. Function does
    not wait for task to be executed and returns immediately after the
    task is put to the queue. Note: Depending on actual platform,
    destruction-time of passed in runnable might be unknown due to
    unpredictability of garbage collection. Therefore, runnable should
    not hold strong references to objects whose lifetimes are critical
    or references should be released at the end of execution.

    </div>

    Parameters:  
    `runnable` -

    Task that should be executed on the main thread. Destruction-time of
    runnable is unknown.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  </div>

</div>

