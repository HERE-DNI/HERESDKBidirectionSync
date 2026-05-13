---
title: "LockingProcess (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LockingProcess.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-..-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-..-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.core.engine.LockingProcess</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LockingProcess</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-..-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>LockingProcess helps to detect situations when cache is locked with another process and
 attempt to create instance of <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> fails with error
 <a href="sdk-for-android-explore-..-errors-instantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER"><code>InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)">destroyLockingProcess</a><wbr/>(android.content.Context context,
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if cache folder is locked.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long)">destroyLockingProcess</a><wbr/>(<a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0, use <a href="#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a> instead.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)">getLockingProcessId</a><wbr/>(android.content.Context context,
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the process ID (PID) that currently locks the map cache or the persistent map storage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLockingProcessId(com.here.sdk.core.engine.SDKOptions)">getLockingProcessId</a><wbr/>(<a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0, use <a href="#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)"><code>getLockingProcessId(android.content.Context, SDKOptions)</code></a> instead.</div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getLockingProcessId(com.here.sdk.core.engine.SDKOptions)">
<h3>getLockingProcessId</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getLockingProcessId</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0, use <a href="#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)"><code>getLockingProcessId(android.content.Context, SDKOptions)</code></a> instead.</p></div>
</div>
<div class="block"><p>Gets the process ID (PID) that currently locks the map cache or the persistent map storage.
 Returns <code>null</code>, when no lock is active. Usually, a lock is not happening on the current process.
 The PID of the current process can be checked with <code>android.os.Process#myPid()</code>.
 The PID can be used to kill or to send a signal to the process with the related functions:
 <code>android.os.Process#killProcess(int)</code> and <code>android.os.Process#sendSignal(int,int)</code>.
 Note that the PID might belong to the current app process, so it is recommended to check this
 before a process is killed as otherwise you will kill your own app process.
 Alternatively, call the convenient function <a href="#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a>.
 </p><p>If a PID is available it means that there is a lock on either the cache or the persistant map storage
 and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider
 to kill the locking process.
 </p><p><strong>Note:</strong>
 The Operation is not atomic and may return a PID for a process which is already destroyed or the file might
 be locked by another thread or process after this function returned <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>The options which are supposed to be used for new instance of the engine.</p></dd>
<dt>Returns:</dt>
<dd><p>Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)">
<h3>getLockingProcessId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getLockingProcessId</span><wbr/><span class="parameters">(@NonNull
 android.content.Context context,
 @NonNull
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> options)</span></div>
<div class="block"><p>Gets the process ID (PID) that currently locks the map cache or the persistent map storage.
 Returns <code>null</code>, when no lock is active. Usually, a lock is not happening on the current process.
 The PID of the current process can be checked with <code>android.os.Process#myPid()</code>.
 The PID can be used to kill or to send a signal to the process with the related functions:
 <code>android.os.Process#killProcess(int)</code> and <code>android.os.Process#sendSignal(int,int)</code>.
 Note that the PID might belong to the current app process, so it is recommended to check this
 before a process is killed as otherwise you will kill your own app process.
 Alternatively, call the convenient function <a href="#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a>.
 </p><p>If a PID is available it means that there is a lock on either the cache or the persistant map storage
 and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider
 to kill the locking process.
 </p><p><strong>Note:</strong>
 The Operation is not atomic and may return a PID for a process which is already destroyed or the file might
 be locked by another thread or process after this function returned <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The Android context</p></dd>
<dd><code>options</code> - <p>The options which are supposed to be used for new instance of the engine.</p></dd>
<dt>Returns:</dt>
<dd><p>Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long)">
<h3>destroyLockingProcess</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">destroyLockingProcess</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0, use <a href="#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)"><code>destroyLockingProcess(android.content.Context, SDKOptions, long)</code></a> instead.</p></div>
</div>
<div class="block"><p>Checks if cache folder is locked. Does nothing if cache is not locked or locked by
 current process. If cache is locked by a different process then the HERE SDK
 makes a few attempts to kill the locking application during the specified timeout.
 If it fails to kill the application, it attempts to remove the cache at
 <a href="sdk-for-android-explore-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>. This function can be used before creating a SDKNativeEngine,
 i.e.
 <pre>
 <code>
      SDKOptions options = new SDKOptions(...);
      LockingProcess.destroyLockingProcess(options, 300);
      SDKNativeEngine engine = new SDKNativeEngine(options);
 </code>
 </pre></p></div>
<dl class="notes">
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
<section class="detail" id="destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)">
<h3>destroyLockingProcess</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">destroyLockingProcess</span><wbr/><span class="parameters">(@NonNull
 android.content.Context context,
 @NonNull
 <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a> sdkOptions,
 long maxTimeoutInMilliseconds)</span></div>
<div class="block"><p>Checks if cache folder is locked. Does nothing if cache is not locked or locked by
 current process. If cache is locked by a different process then the HERE SDK
 makes a few attempts to kill the locking application during the specified timeout.
 If it fails to kill the application, it attempts to remove the cache at
 <a href="sdk-for-android-explore-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>. This function can be used before creating a SDKNativeEngine,
 i.e.
 <pre>
 <code>
      SDKOptions options = new SDKOptions(...);
      LockingProcess.destroyLockingProcess(context, options, 300);
      SDKNativeEngine engine = new SDKNativeEngine(options);
 </code>
 </pre></p></div>
<dl class="notes">
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
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
