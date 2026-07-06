---
title: "LockingProcess (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.core.engine.LockingProcess →
com.here.NativeBase → com.here.sdk.core.engine.LockingProcess

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">LockingProcess</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

LockingProcess helps to detect situations when cache is locked with
another process and attempt to create instance of SDKNativeEngine fails
with error InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER .

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      destroyLockingProcess(android.content.Context context,
       SDKOptions sdkOptions,
       long maxTimeoutInMilliseconds)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Checks if cache folder is locked.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

      destroyLockingProcess(SDKOptions sdkOptions,
       long maxTimeoutInMilliseconds)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.27.0, use
  destroyLockingProcess(android.content.Context, SDKOptions, long)
  instead.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getLockingProcessId(android.content.Context context,
       SDKOptions options)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets the process ID (PID) that currently locks the map cache or the
  persistent map storage.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  `static `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

      getLockingProcessId(SDKOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.27.0, use
  getLockingProcessId(android.content.Context, SDKOptions) instead.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-getLockingProcessId(com.here.sdk.core.engine.SDKOptions)"
    class="section detail">

    ### getLockingProcessId

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getLockingProcessId</span><span class="parameters">(@NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") options)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0, use
    [](sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions))

        getLockingProcessId(android.content.Context, SDKOptions)

    instead.

    </div>

    </div>

    <div class="block">

    Gets the process ID (PID) that currently locks the map cache or the
    persistent map storage. Returns null , when no lock is active.
    Usually, a lock is not happening on the current process. The PID of
    the current process can be checked with android.os.Process#myPid() .
    The PID can be used to kill or to send a signal to the process with
    the related functions: android.os.Process#killProcess(int) and
    android.os.Process#sendSignal(int,int) . Note that the PID might
    belong to the current app process, so it is recommended to check
    this before a process is killed as otherwise you will kill your own
    app process. Alternatively, call the convenient function
    destroyLockingProcess(android.content.Context, SDKOptions, long) .
    If a PID is available it means that there is a lock on either the
    cache or the persistant map storage and that the HERE SDK will be
    non-functional until the locking process is killed. In such a case,
    consider to kill the locking process. Note: The Operation is not
    atomic and may return a PID for a process which is already destroyed
    or the file might be locked by another thread or process after this
    function returned null .

    </div>

    Parameters:  
    `options` -

    The options which are supposed to be used for new instance of the
    engine.

    Returns:  
    Process ID if the cache or the persistent map directory is locked
    and a process ID was successfully read.

    </div>
<div id="sdk-for-android-explore-getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)"
    class="section detail">

    ### getLockingProcessId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getLockingProcessId</span><span class="parameters">(@NonNull
    android.content.Context context, @NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") options)</span>

    </div>

    <div class="block">

    Gets the process ID (PID) that currently locks the map cache or the
    persistent map storage. Returns null , when no lock is active.
    Usually, a lock is not happening on the current process. The PID of
    the current process can be checked with android.os.Process#myPid() .
    The PID can be used to kill or to send a signal to the process with
    the related functions: android.os.Process#killProcess(int) and
    android.os.Process#sendSignal(int,int) . Note that the PID might
    belong to the current app process, so it is recommended to check
    this before a process is killed as otherwise you will kill your own
    app process. Alternatively, call the convenient function
    destroyLockingProcess(android.content.Context, SDKOptions, long) .
    If a PID is available it means that there is a lock on either the
    cache or the persistant map storage and that the HERE SDK will be
    non-functional until the locking process is killed. In such a case,
    consider to kill the locking process. Note: The Operation is not
    atomic and may return a PID for a process which is already destroyed
    or the file might be locked by another thread or process after this
    function returned null .

    </div>

    Parameters:  
    `context` -

    The Android context

    `options` -

    The options which are supposed to be used for new instance of the
    engine.

    Returns:  
    Process ID if the cache or the persistent map directory is locked
    and a process ID was successfully read.

    </div>
<div id="sdk-for-android-explore-destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long)"
    class="section detail">

    ### destroyLockingProcess

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">destroyLockingProcess</span><span class="parameters">(@NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") sdkOptions,
    long maxTimeoutInMilliseconds)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0, use
    [](sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long))

        destroyLockingProcess(android.content.Context, SDKOptions, long)

    instead.

    </div>

    </div>

    <div class="block">

    Checks if cache folder is locked. Does nothing if cache is not
    locked or locked by current process. If cache is locked by a
    different process then the HERE SDK makes a few attempts to kill the
    locking application during the specified timeout. If it fails to
    kill the application, it attempts to remove the cache at
    SDKOptions.cachePath . This function can be used before creating a
    SDKNativeEngine, i.e. SDKOptions options = new SDKOptions(...);
    LockingProcess.destroyLockingProcess(options, 300); SDKNativeEngine
    engine = new SDKNativeEngine(options);

    </div>

    Parameters:  
    `sdkOptions` -

    The options which are supposed to be used for a new instance of the
    engine.

    `maxTimeoutInMilliseconds` -

    The maximum timeout in milliseconds. Recommended value is 300 - 500
    milliseconds. If 0 or a negative value is passed then it makes only
    one attempt to kill the locking process (if any) and waits 30
    milliseconds before exit because the system may spend a small amount
    of time to perform the operation.

    </div>
<div id="sdk-for-android-explore-destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"
    class="section detail">

    ### destroyLockingProcess

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">destroyLockingProcess</span><span class="parameters">(@NonNull
    android.content.Context context, @NonNull
    [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine") sdkOptions,
    long maxTimeoutInMilliseconds)</span>

    </div>

    <div class="block">

    Checks if cache folder is locked. Does nothing if cache is not
    locked or locked by current process. If cache is locked by a
    different process then the HERE SDK makes a few attempts to kill the
    locking application during the specified timeout. If it fails to
    kill the application, it attempts to remove the cache at
    SDKOptions.cachePath . This function can be used before creating a
    SDKNativeEngine, i.e. SDKOptions options = new SDKOptions(...);
    LockingProcess.destroyLockingProcess(context, options, 300);
    SDKNativeEngine engine = new SDKNativeEngine(options);

    </div>

    Parameters:  
    `context` -

    The Android context

    `sdkOptions` -

    The options which are supposed to be used for a new instance of the
    engine.

    `maxTimeoutInMilliseconds` -

    The maximum timeout in milliseconds. Recommended value is 300 - 500
    milliseconds. If 0 or a negative value is passed then it makes only
    one attempt to kill the locking process (if any) and waits 30
    milliseconds before exit because the system may spend a small amount
    of time to perform the operation.

    </div>

  </div>

</div>

