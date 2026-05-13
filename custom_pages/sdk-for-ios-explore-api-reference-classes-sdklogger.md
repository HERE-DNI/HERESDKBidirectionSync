---
title: "SDKLogger Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-sdklogger"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SDKLogger.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/SDKLogger"></a>
<a title="SDKLogger Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SDKLogger Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class SDKLogger</code></pre>
<pre><code>extension SDKLogger: NativeBase</code></pre>
<pre><code>extension SDKLogger: Hashable</code></pre>
</div>
</div>
<p>Logging interface for Android/iOS platforms.
These logs are under management of <code><a href="sdk-for-ios-explore-api-reference-..-classes-logcontrol">LogControl</a></code> and should be used instead of platform-specific logging functions.</p>
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
<pre><code>public static func log(level: LogLevel, tag: String, message: String)</code></pre>
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
<pre><code>public static func info(tag: String, message: String)</code></pre>
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
<pre><code>public static func warn(tag: String, message: String)</code></pre>
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
<pre><code>public static func error(tag: String, message: String)</code></pre>
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
<pre><code>public static func fatal(tag: String, message: String)</code></pre>
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



</div>
`
}</HTMLBlock>
