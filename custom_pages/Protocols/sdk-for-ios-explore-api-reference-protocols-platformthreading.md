---
title: "PlatformThreading Protocol Reference"
slug: "sdk-for-ios-explore-api-reference-protocols-platformthreading"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PlatformThreading.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Protocol/PlatformThreading"></a>
<a title="PlatformThreading Protocol Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Core.html">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PlatformThreading Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public protocol PlatformThreading : AnyObject</code></pre>
</div>
</div>
<p>Protocol for task activities on the main thread.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PlatformThreadingP15runOnMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/runOnMainThread(runnable:)"></a>
<a class="token" href="#/s:7heresdk17PlatformThreadingP15runOnMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF">runOnMainThread(runnable:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Runs a task on the main thread.
If this function is called from the main thread, then the task will run immediately. Otherwise,
it is put to the end of the queue of the main thread.
Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
to unpredictability of garbage collection. Therefore, runnable should not hold strong references
to objects whose lifetimes are critical or references should be released at the end of execution.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>func runOnMainThread(runnable: Runnable) -&gt; TaskHandle</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>runnable</em>
</code>
</td>
<td>
<div>
<p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PlatformThreadingP16postToMainThread8runnable7delayMsAA10TaskHandle_pAA8Runnable_p_s6UInt64VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/postToMainThread(runnable:delayMs:)"></a>
<a class="token" href="#/s:7heresdk17PlatformThreadingP16postToMainThread8runnable7delayMsAA10TaskHandle_pAA8Runnable_p_s6UInt64VtF">postToMainThread(runnable:<wbr/>delayMs:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Posts a task to be executed on the main thread after some delay.
If the delay is 0, the function puts the task at the end of the queue.
The function does not wait for the task to be executed and returns immediately after the task
has been put in the queue.
Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
to unpredictability of garbage collection. Therefore, runnable should not hold strong references
to objects whose lifetimes are critical or references should be released at the end of execution.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>func postToMainThread(runnable: Runnable, delayMs: UInt64) -&gt; TaskHandle</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>runnable</em>
</code>
</td>
<td>
<div>
<p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delayMs</em>
</code>
</td>
<td>
<div>
<p>Delay in milliseconds.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PlatformThreadingP16postToMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/postToMainThread(runnable:)"></a>
<a class="token" href="#/s:7heresdk17PlatformThreadingP16postToMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF">postToMainThread(runnable:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Posts task to the end of the queue of the main thread.
Function does not wait for task to be executed and returns immediately after the task is put to the queue.
Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due
to unpredictability of garbage collection. Therefore, runnable should not hold strong references
to objects whose lifetimes are critical or references should be released at the end of execution.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>func postToMainThread(runnable: Runnable) -&gt; TaskHandle</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>runnable</em>
</code>
</td>
<td>
<div>
<p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate execution of the task.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
