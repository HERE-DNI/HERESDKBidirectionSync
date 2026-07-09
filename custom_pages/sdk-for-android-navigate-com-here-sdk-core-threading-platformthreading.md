---
title: "PlatformThreading (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-threading-platformthreading"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PlatformThreading.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.threading</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">PlatformThreading</span></div>
<div className="block"><p>Interface for task activities on the main thread.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="runOnMainThread(com.here.sdk.core.threading.Runnable)">
<h3>runOnMainThread</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">runOnMainThread</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</span></div>
<div className="block"><p>Runs a task on the main thread.
 If this function is called from the main thread, then the task will run immediately. Otherwise,
 it is put to the end of the queue of the main thread.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="postToMainThread(com.here.sdk.core.threading.Runnable,long)">
<h3>postToMainThread</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">postToMainThread</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable,
 long delayMs)</span></div>
<div className="block"><p>Posts a task to be executed on the main thread after some delay.
 If the delay is 0, the function puts the task at the end of the queue.
 The function does not wait for the task to be executed and returns immediately after the task
 has been put in the queue.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p></dd>
<dd><code>delayMs</code> - <p>Delay in milliseconds.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="postToMainThread(com.here.sdk.core.threading.Runnable)">
<h3>postToMainThread</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">postToMainThread</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-runnable" title="interface in com.here.sdk.core.threading">Runnable</a> runnable)</span></div>
<div className="block"><p>Posts task to the end of the queue of the main thread.
 Function does not wait for task to be executed and returns immediately after the task is put to the queue.
 Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
 to unpredictability of garbage collection. Therefore, runnable should not hold strong references
 to objects whose lifetimes are critical or references should be released at the end of execution.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
