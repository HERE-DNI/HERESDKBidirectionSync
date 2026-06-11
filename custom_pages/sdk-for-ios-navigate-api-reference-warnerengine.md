---
title: "sdk-for-ios-navigate-api-reference-warnerengine"
slug: "sdk-for-ios-navigate-api-reference-warnerengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/WarnerEngine"></a>
<a title="WarnerEngine  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
        WarnerEngine  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>WarnerEngine</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CustomWarning"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV">CustomWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>struct container for custom warning data.</p>
<p>This structure represents the type-specific payload associated
with a custom warning.</p>
<p>Instances of this structure are typically produced by custom warning
evaluation logic and may also be retrieved from the <code>WarningRegistry</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-customwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CustomWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21CustomWarningProviderP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CustomWarningProvider"></a>
<a class="token" href="#/s:7heresdk21CustomWarningProviderP">CustomWarningProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A protocol representing a provider of custom warnings based on vehicle position.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-customwarningprovider">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CustomWarningProvider</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Warning"></a>
<a class="token" href="#/s:7heresdk7WarningV">Warning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct which represents a warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-warning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Warning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/WarnerEngine"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC">WarnerEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the core functionality for generating and managing navigation warnings.</p>
<p><code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
of warnings should be issued. It is used with <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code>,
which supply the road topology and positional updates required for warning evaluation.</p>
<p>The engine monitors enabled warning types and notifies registered listeners when new warnings become available.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-warnerengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">WarnerEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarnerEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarnerEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15WarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/WarningDelegate"></a>
<a class="token" href="#/s:7heresdk15WarningDelegateP">WarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A generic listener interface protocol for receiving warning notifications.</p>
<p>Implementations of this interface are notified whenever the <code><a href="sdk-for-ios-navigate-api-reference-classes-warnerengine">WarnerEngine</a></code> detects new warnings.
The listener receives a list of <code><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></code> objects, each describing a specific event or condition that requires user attention.</p>
<p>Classes interested in warning updates should implement this listener
and register themselves via <code>WarnerEngine.addWarningListener</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-warningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">WarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14WarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WarningOptions"></a>
<a class="token" href="#/s:7heresdk14WarningOptionsV">WarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct with options to configure <code><a href="Classes/WarnerEngine.html#/s:7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp">WarnerEngine.warningOptions</a></code></p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-warningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/WarningsRegistry"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC">WarningsRegistry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class that store warning metadata for different warning types.
Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.).
Provided by <code><a href="sdk-for-ios-navigate-api-reference-classes-warnerengine">WarnerEngine</a></code> so callers can lookup detailed information about specific warnings.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-warningsregistry">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">WarningsRegistry</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarningsRegistry</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarningsRegistry</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

`
}</HTMLBlock>
