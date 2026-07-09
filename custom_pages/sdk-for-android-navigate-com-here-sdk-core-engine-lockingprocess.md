---
title: "LockingProcess (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-lockingprocess"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LockingProcess.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.LockingProcess</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LockingProcess</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>LockingProcess helps to detect situations when cache is locked with another process and
 attempt to create instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> fails with error
 <a href="sdk-for-android-navigate-instantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER"><code>InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getLockingProcessId(com.here.sdk.core.engine.SDKOptions)">
<h3>getLockingProcessId</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">getLockingProcessId</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0, use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-lockingprocess#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)"><code>getLockingProcessId(android.content.Context, SDKOptions)</code></a> instead.</p></div>
</div>
<div className="block"><p>Gets the process ID (PID) that currently locks the map cache or the persistent map storage.
 Returns <code>null</code>, when no lock is active. Usually, a lock is not happening on the current process.
 The PID of the current process can be checked with <code>android.os.Process#myPid()</code>.
 The PID can be used to kill or to send a signal to the process with the related functions:
 <code>android.os.Process#killProcess(int)</code> and <code>android.os.Process#sendSignal(int,int)</code>.
 Note that the PID might belong to the current app process, so it is recommended to check this
 before a process is killed as otherwise you will kill your own app process.
 Alternatively, call the convenient function <a href="sdk-for-android-navigate-com-here-sdk-core-engine-lockingprocess#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a>.
 If a PID is available it means that there is a lock on either the cache or the persistant map storage
 and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider
 to kill the locking process.
 <strong>Note:</strong>
 The Operation is not atomic and may return a PID for a process which is already destroyed or the file might
 be locked by another thread or process after this function returned <code>null</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>The options which are supposed to be used for new instance of the engine.</p></dd>
<dt>Returns:</dt>
<dd><p>Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>getLockingProcessId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">getLockingProcessId</span><wbr/><span className="parameters">(@NonNull
 android.content.Context context,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span></div>
<div className="block"><p>Gets the process ID (PID) that currently locks the map cache or the persistent map storage.
 Returns <code>null</code>, when no lock is active. Usually, a lock is not happening on the current process.
 The PID of the current process can be checked with <code>android.os.Process#myPid()</code>.
 The PID can be used to kill or to send a signal to the process with the related functions:
 <code>android.os.Process#killProcess(int)</code> and <code>android.os.Process#sendSignal(int,int)</code>.
 Note that the PID might belong to the current app process, so it is recommended to check this
 before a process is killed as otherwise you will kill your own app process.
 Alternatively, call the convenient function <a href="sdk-for-android-navigate-com-here-sdk-core-engine-lockingprocess#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a>.
 If a PID is available it means that there is a lock on either the cache or the persistant map storage
 and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider
 to kill the locking process.
 <strong>Note:</strong>
 The Operation is not atomic and may return a PID for a process which is already destroyed or the file might
 be locked by another thread or process after this function returned <code>null</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options which are supposed to be used for new instance of the engine.</p></dd>
<dt>Returns:</dt>
<dd><p>Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long)">
<h3>destroyLockingProcess</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">destroyLockingProcess</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0, use <a href="sdk-for-android-navigate-com-here-sdk-core-engine-lockingprocess#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a> instead.</p></div>
</div>
<div className="block"><p>Checks if cache folder is locked. Does nothing if cache is not locked or locked by
 current process. If cache is locked by a different process then the HERE SDK
 makes a few attempts to kill the locking application during the specified timeout.
 If it fails to kill the application, it attempts to remove the cache at
 <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>. This function can be used before creating a SDKNativeEngine,
 i.e.
 <pre>
 <code>
      SDKOptions options = new SDKOptions(...);
      LockingProcess.destroyLockingProcess(options, 300);
      SDKNativeEngine engine = new SDKNativeEngine(options);
 </code>
 </pre></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkOptions</code> - <p>The options which are supposed to be used for a new instance of the engine.</p></dd>
<dd><code>maxTimeoutInMilliseconds</code> - <p>The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds.
     If 0 or a negative value is passed then it makes only one attempt to kill the locking
     process (if any) and waits 30 milliseconds before exit because the system may spend a
     small amount of time to perform the operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)">
<h3>destroyLockingProcess</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">destroyLockingProcess</span><wbr/><span className="parameters">(@NonNull
 android.content.Context context,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</span></div>
<div className="block"><p>Checks if cache folder is locked. Does nothing if cache is not locked or locked by
 current process. If cache is locked by a different process then the HERE SDK
 makes a few attempts to kill the locking application during the specified timeout.
 If it fails to kill the application, it attempts to remove the cache at
 <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>. This function can be used before creating a SDKNativeEngine,
 i.e.
 <pre>
 <code>
      SDKOptions options = new SDKOptions(...);
      LockingProcess.destroyLockingProcess(context, options, 300);
      SDKNativeEngine engine = new SDKNativeEngine(options);
 </code>
 </pre></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The Android context</p></dd>
<dd><code>sdkOptions</code> - <p>The options which are supposed to be used for a new instance of the engine.</p></dd>
<dd><code>maxTimeoutInMilliseconds</code> - <p>The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds.
     If 0 or a negative value is passed then it makes only one attempt to kill the locking
     process (if any) and waits 30 milliseconds before exit because the system may spend a
     small amount of time to perform the operation.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
