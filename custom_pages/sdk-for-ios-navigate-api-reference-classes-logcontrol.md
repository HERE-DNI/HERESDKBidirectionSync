---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-logcontrol"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LogControl.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LogControl"></a>
<a title="LogControl Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LogControl Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LogControl</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LogControl</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LogControl</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LogControl</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides functionality to enable/disable console logs as well as
setting a custom log appender to receive log messages from the SDK.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC16InvalidPathErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InvalidPathError"></a>
<a class="token" href="#/s:7heresdk10LogControlC16InvalidPathErrora">InvalidPathError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid file path exception.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InvalidPathError</span> <span class="o">=</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC22enableLoggingToConsole5levelyAA0B5LevelO_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/enableLoggingToConsole(level:)"></a>
<a class="token" href="#/s:7heresdk10LogControlC22enableLoggingToConsole5levelyAA0B5LevelO_tFZ">enableLoggingToConsole(level:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables SDK logging messages to console that can be viewed using macOS Console app.
Enabled by default with <code><a href="../Enums/LogLevel.html#/s:7heresdk8LogLevelO03logC4InfoyA2CmF">LogLevel.logLevelInfo</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">enableLoggingToConsole</span><span class="p">(</span><span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-loglevel">LogLevel</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>level</em>
</code>
</td>
<td>
<div>
<p>Log level.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC23disableLoggingToConsoleyyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/disableLoggingToConsole()"></a>
<a class="token" href="#/s:7heresdk10LogControlC23disableLoggingToConsoleyyFZ">disableLoggingToConsole()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Disables SDK logging messages to console. Enabled by default with <code><a href="../Enums/LogLevel.html#/s:7heresdk8LogLevelO03logC4InfoyA2CmF">LogLevel.logLevelInfo</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">disableLoggingToConsole</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC11setAppender5level8appenderyAA0B5LevelO_AA0bE0_ptFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAppender(level:appender:)"></a>
<a class="token" href="#/s:7heresdk10LogControlC11setAppender5level8appenderyAA0B5LevelO_AA0bE0_ptFZ">setAppender(level:<wbr/>appender:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom log appender to receive log messages from the SDK.
This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use <code><a href="../Classes/LogControl.html#/s:7heresdk10LogControlC23disableLoggingToConsoleyyFZ">LogControl.disableLoggingToConsole(...)</a></code> API.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setAppender</span><span class="p">(</span><span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-loglevel">LogLevel</a></span><span class="p">,</span> <span class="nv">appender</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-logappender">LogAppender</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>level</em>
</code>
</td>
<td>
<div>
<p>Log level.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>appender</em>
</code>
</td>
<td>
<div>
<p>New log appender.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC11setAppender5level4pathyAA0B5LevelO_SStKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAppender(level:path:)"></a>
<a class="token" href="#/s:7heresdk10LogControlC11setAppender5level4pathyAA0B5LevelO_SStKFZ">setAppender(level:<wbr/>path:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom log appender that will write SDK log messages to a file.
This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use <code><a href="../Classes/LogControl.html#/s:7heresdk10LogControlC23disableLoggingToConsoleyyFZ">LogControl.disableLoggingToConsole(...)</a></code> API.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/LogControl.html#/s:7heresdk10LogControlC16InvalidPathErrora">LogControl.InvalidPathError</a></code> <code><a href="../Classes/LogControl.html#/s:7heresdk10LogControlC16InvalidPathErrora">LogControl.InvalidPathError</a></code> Indicates that the file path is invalid or not writeable.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setAppender</span><span class="p">(</span><span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-loglevel">LogLevel</a></span><span class="p">,</span> <span class="nv">path</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>level</em>
</code>
</td>
<td>
<div>
<p>Log level.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>path</em>
</code>
</td>
<td>
<div>
<p>Absolute path to a file that the application has read/write permissions.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC14removeAppenderyyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAppender()"></a>
<a class="token" href="#/s:7heresdk10LogControlC14removeAppenderyyFZ">removeAppender()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes previously added custom log appender.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">removeAppender</span><span class="p">()</span></code></pre>
</div>
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

</div>
`
}</HTMLBlock>
