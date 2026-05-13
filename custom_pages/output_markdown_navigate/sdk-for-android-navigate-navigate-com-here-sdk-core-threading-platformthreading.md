---
title: "PlatformThreading (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-core-threading-platformthreading"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PlatformThreading.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.threading</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PlatformThreading</span></div>
<div class="block"><p>Interface for task activities on the main thread.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#postToMainThread(com.here.sdk.core.threading.Runnable)">postToMainThread</a><wbr/>(<a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Posts task to the end of the queue of the main thread.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#postToMainThread(com.here.sdk.core.threading.Runnable,long)">postToMainThread</a><wbr/>(<a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable,
 long delayMs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Posts a task to be executed on the main thread after some delay.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#runOnMainThread(com.here.sdk.core.threading.Runnable)">runOnMainThread</a><wbr/>(<a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Runs a task on the main thread.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="runOnMainThread(com.here.sdk.core.threading.Runnable)">
<h3>runOnMainThread</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">runOnMainThread</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</span></div>
<div class="block"><p>Runs a task on the main thread.
 If this function is called from the main thread, then the task will run immediately. Otherwise,
 it is put to the end of the queue of the main thread.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postToMainThread(com.here.sdk.core.threading.Runnable,long)">
<h3>postToMainThread</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">postToMainThread</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable,
 long delayMs)</span></div>
<div class="block"><p>Posts a task to be executed on the main thread after some delay.
 If the delay is 0, the function puts the task at the end of the queue.
 The function does not wait for the task to be executed and returns immediately after the task
 has been put in the queue.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p></dd>
<dd><code>delayMs</code> - <p>Delay in milliseconds.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postToMainThread(com.here.sdk.core.threading.Runnable)">
<h3>postToMainThread</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">postToMainThread</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</span></div>
<div class="block"><p>Posts task to the end of the queue of the main thread.
 Function does not wait for task to be executed and returns immediately after the task is put to the queue.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
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
