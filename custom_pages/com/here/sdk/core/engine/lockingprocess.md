---
title: "LockingProcess (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlockingprocess"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LockingProcess

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.LockingProcess
------------------------------------------------------------------------
public final class LockingProcess extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") fails with error [`InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER).

## Method Summary

  All Methods
  Static Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `static void`

  [destroyLockingProcess](#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long))`(android.content.Context context, `[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` sdkOptions, long maxTimeoutInMilliseconds)`

Checks if cache folder is locked.

`static void`

  [destroyLockingProcess](#destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long))`(`[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` sdkOptions, long maxTimeoutInMilliseconds)`

Deprecated.
Will be removed in v4.27.0, use [`destroyLockingProcess(android.content.Context, SDKOptions, long)`](#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)) instead.

  `static `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [getLockingProcessId](#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions))`(android.content.Context context, `[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` options)`

Gets the process ID (PID) that currently locks the map cache or the persistent map storage.

`static `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [getLockingProcessId](#getLockingProcessId(com.here.sdk.core.engine.SDKOptions))`(`[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` options)`

Deprecated.
Will be removed in v4.27.0, use [`getLockingProcessId(android.content.Context, SDKOptions)`](#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)) instead.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getLockingProcessId

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public static [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getLockingProcessId(@NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") options)

    Deprecated.
Will be removed in v4.27.0, use [`getLockingProcessId(android.content.Context, SDKOptions)`](#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)) instead.

Gets the process ID (PID) that currently locks the map cache or the persistent map storage. Returns `null`, when no lock is active. Usually, a lock is not happening on the current process. The PID of the current process can be checked with `android.os.Process#myPid()`. The PID can be used to kill or to send a signal to the process with the related functions: `android.os.Process#killProcess(int)` and `android.os.Process#sendSignal(int,int)`. Note that the PID might belong to the current app process, so it is recommended to check this before a process is killed as otherwise you will kill your own app process. Alternatively, call the convenient function [`destroyLockingProcess(android.content.Context, SDKOptions, long)`](#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)).

    If a PID is available it means that there is a lock on either the cache or the persistant map storage and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider to kill the locking process.

    **Note:** The Operation is not atomic and may return a PID for a process which is already destroyed or the file might be locked by another thread or process after this function returned `null`.
Parameters:
    `options` -

    The options which are supposed to be used for new instance of the engine.

    Returns:
    Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.

### getLockingProcessId

@Nullable public static [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getLockingProcessId(@NonNull android.content.Context context, @NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") options)

    Gets the process ID (PID) that currently locks the map cache or the persistent map storage. Returns `null`, when no lock is active. Usually, a lock is not happening on the current process. The PID of the current process can be checked with `android.os.Process#myPid()`. The PID can be used to kill or to send a signal to the process with the related functions: `android.os.Process#killProcess(int)` and `android.os.Process#sendSignal(int,int)`. Note that the PID might belong to the current app process, so it is recommended to check this before a process is killed as otherwise you will kill your own app process. Alternatively, call the convenient function [`destroyLockingProcess(android.content.Context, SDKOptions, long)`](#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)).

    If a PID is available it means that there is a lock on either the cache or the persistant map storage and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider to kill the locking process.

    **Note:** The Operation is not atomic and may return a PID for a process which is already destroyed or the file might be locked by another thread or process after this function returned `null`.
Parameters:
    `context` -

    The Android context

    `options` -

    The options which are supposed to be used for new instance of the engine.

    Returns:
    Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.

### destroyLockingProcess

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public static void destroyLockingProcess(@NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") sdkOptions, long maxTimeoutInMilliseconds)

    Deprecated.
Will be removed in v4.27.0, use [`destroyLockingProcess(android.content.Context, SDKOptions, long)`](#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)) instead.

Checks if cache folder is locked. Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at [`SDKOptions.cachePath`](sdk-for-android-explore-api-reference-latestsdkoptions#cachePath). This function can be used before creating a SDKNativeEngine, i.e.

              SDKOptions options = new SDKOptions(...);
              LockingProcess.destroyLockingProcess(options, 300);
              SDKNativeEngine engine = new SDKNativeEngine(options);
Parameters:
    `sdkOptions` -

    The options which are supposed to be used for a new instance of the engine.

    `maxTimeoutInMilliseconds` -

    The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds. If 0 or a negative value is passed then it makes only one attempt to kill the locking process (if any) and waits 30 milliseconds before exit because the system may spend a small amount of time to perform the operation.

### destroyLockingProcess

public static void destroyLockingProcess(@NonNull android.content.Context context, @NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") sdkOptions, long maxTimeoutInMilliseconds)

    Checks if cache folder is locked. Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at [`SDKOptions.cachePath`](sdk-for-android-explore-api-reference-latestsdkoptions#cachePath). This function can be used before creating a SDKNativeEngine, i.e.

              SDKOptions options = new SDKOptions(...);
              LockingProcess.destroyLockingProcess(context, options, 300);
              SDKNativeEngine engine = new SDKNativeEngine(options);
Parameters:
    `context` -

    The Android context

    `sdkOptions` -

    The options which are supposed to be used for a new instance of the engine.

    `maxTimeoutInMilliseconds` -

    The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds. If 0 or a negative value is passed then it makes only one attempt to kill the locking process (if any) and waits 30 milliseconds before exit because the system may spend a small amount of time to perform the operation.
