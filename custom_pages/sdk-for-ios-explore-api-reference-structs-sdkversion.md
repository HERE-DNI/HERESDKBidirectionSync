---
title: "SDKVersion Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-sdkversion"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SDKVersion.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/SDKVersion"></a>
<a title="SDKVersion Structure Reference"></a>
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
        SDKVersion Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct SDKVersion : Hashable</code></pre>
</div>
</div>
<p>The <code>SDKVersion</code> represents version information for an SDK product. It encapsulates
various attributes related to the version, including product variant, version details and
backend configuration.
Please note, <code>sdk.core.engine.SDKBuildInformation</code> can be used to get <code>SDKVersion</code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV14productVariantSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/productVariant"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV14productVariantSSvp">productVariant</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Product variant.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var productVariant: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV11versionNameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionName"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV11versionNameSSvp">versionName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Version information as string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionName: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV17versionGenerations5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionGeneration"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV17versionGenerations5Int32Vvp">versionGeneration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Generation number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionGeneration: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV12versionMajors5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionMajor"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV12versionMajors5Int32Vvp">versionMajor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Major version number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionMajor: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV12versionMinors5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionMinor"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV12versionMinors5Int32Vvp">versionMinor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minor version number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionMinor: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV12versionPatchs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionPatch"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV12versionPatchs5Int32Vvp">versionPatch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Patch number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionPatch: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV12versionBuilds5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionBuild"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV12versionBuilds5Int32Vvp">versionBuild</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Build number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionBuild: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV10versionTagSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/versionTag"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV10versionTagSSvp">versionTag</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Version tag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var versionTag: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV13backendConfigSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/backendConfig"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV13backendConfigSSvp">backendConfig</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Backend config</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var backendConfig: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV14productVariant11versionName0E10Generation0E5Major0E5Minor0E5Patch0E5Build0E3Tag13backendConfigACSS_SSs5Int32VA4NS2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(productVariant:versionName:versionGeneration:versionMajor:versionMinor:versionPatch:versionBuild:versionTag:backendConfig:)"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV14productVariant11versionName0E10Generation0E5Major0E5Minor0E5Patch0E5Build0E3Tag13backendConfigACSS_SSs5Int32VA4NS2Stcfc">init(productVariant:<wbr/>versionName:<wbr/>versionGeneration:<wbr/>versionMajor:<wbr/>versionMinor:<wbr/>versionPatch:<wbr/>versionBuild:<wbr/>versionTag:<wbr/>backendConfig:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new SDK version instance from the provided parameter values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(productVariant: String, versionName: String, versionGeneration: Int32, versionMajor: Int32, versionMinor: Int32, versionPatch: Int32, versionBuild: Int32, versionTag: String, backendConfig: String)</code></pre>
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



</div>
`
}</HTMLBlock>
