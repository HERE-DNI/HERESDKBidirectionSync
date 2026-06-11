---
title: "SDKLogger"
slug: "sdk-for-ios-navigate-api-reference-classes-sdklogger"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKLogger"></a>
<a title="SDKLogger Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        SDKLogger Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SDKLogger</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SDKLogger</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKLogger</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKLogger</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Logging interface for Android/iOS platforms.
These logs are under management of <code><a href="sdk-for-ios-navigate-api-reference-classes-logcontrol">LogControl</a></code> and should be used instead of platform-specific logging functions.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9SDKLoggerC3log5level3tag7messageyAA8LogLevelO_S2StFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/log(level:tag:message:)"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC3log5level3tag7messageyAA8LogLevelO_S2StFZ">log(level:<wbr/>tag:<wbr/>message:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">log</span><span class="p">(</span><span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-loglevel">LogLevel</a></span><span class="p">,</span> <span class="nv">tag</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">message</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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
<p>The severity of the log message.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tag</em>
</code>
</td>
<td>
<div>
<p>The log tag.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>message</em>
</code>
</td>
<td>
<div>
<p>The log message.</p>
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
<a name="/s:7heresdk9SDKLoggerC4info3tag7messageySS_SStFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/info(tag:message:)"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC4info3tag7messageySS_SStFZ">info(tag:<wbr/>message:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>convenient function to print a message with log level INFO and tag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">info</span><span class="p">(</span><span class="nv">tag</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">message</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tag</em>
</code>
</td>
<td>
<div>
<p>The log tag.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>message</em>
</code>
</td>
<td>
<div>
<p>The log message.</p>
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
<a name="/s:7heresdk9SDKLoggerC4warn3tag7messageySS_SStFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/warn(tag:message:)"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC4warn3tag7messageySS_SStFZ">warn(tag:<wbr/>message:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>convenient function to print a message with log level WARNING and tag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">warn</span><span class="p">(</span><span class="nv">tag</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">message</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tag</em>
</code>
</td>
<td>
<div>
<p>The log tag.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>message</em>
</code>
</td>
<td>
<div>
<p>The log message.</p>
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
<a name="/s:7heresdk9SDKLoggerC5error3tag7messageySS_SStFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/error(tag:message:)"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC5error3tag7messageySS_SStFZ">error(tag:<wbr/>message:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>convenient function to print a message with log level ERROR and tag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">error</span><span class="p">(</span><span class="nv">tag</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">message</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tag</em>
</code>
</td>
<td>
<div>
<p>The log tag.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>message</em>
</code>
</td>
<td>
<div>
<p>The log message.</p>
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
<a name="/s:7heresdk9SDKLoggerC5fatal3tag7messageySS_SStFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fatal(tag:message:)"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC5fatal3tag7messageySS_SStFZ">fatal(tag:<wbr/>message:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>convenient function to print a message with log level FATAL and tag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fatal</span><span class="p">(</span><span class="nv">tag</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">message</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tag</em>
</code>
</td>
<td>
<div>
<p>The log tag.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>message</em>
</code>
</td>
<td>
<div>
<p>The log message.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
}</HTMLBlock>
