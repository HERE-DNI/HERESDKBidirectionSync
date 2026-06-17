---
title: "PlatformThreading"
slug: "sdk-for-ios-explore-protocols-platformthreading"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PlatformThreading"></a>
<a title="PlatformThreading Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-core">Core</a>

        PlatformThreading Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PlatformThreading</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PlatformThreading</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">runOnMainThread</span><span class="p">(</span><span class="nv">runnable</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-runnable">Runnable</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">postToMainThread</span><span class="p">(</span><span class="nv">runnable</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-runnable">Runnable</a></span><span class="p">,</span> <span class="nv">delayMs</span><span class="p">:</span> <span class="kt">UInt64</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">postToMainThread</span><span class="p">(</span><span class="nv">runnable</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-runnable">Runnable</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
</body>
</html>

`
} </HTMLBlock>
