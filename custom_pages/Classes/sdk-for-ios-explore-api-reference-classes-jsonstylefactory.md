---
title: "JsonStyleFactory Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-jsonstylefactory"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- JsonStyleFactory.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/JsonStyleFactory"></a>
<a title="JsonStyleFactory Class Reference"></a>
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
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        JsonStyleFactory Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class JsonStyleFactory</code></pre>
<pre><code>extension JsonStyleFactory: NativeBase</code></pre>
<pre><code>extension JsonStyleFactory: Hashable</code></pre>
</div>
</div>
<p>A factory of <code><a href="../Classes/Style.html">Style</a></code> objects from styles defined in JSON format.
For more details see Custom Layer Style Reference in the documentation.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when failing to create a <code><a href="../Classes/Style.html">Style</a></code> from a JSON source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias InstantiationError = InstantiationErrorDetails</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes reasons for failing to create a <code><a href="../Classes/Style.html">Style</a></code> from a JSON source.</p>
<a class="slightly-smaller" href="../Classes/JsonStyleFactory/InstantiationErrorCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstantiationErrorDetails"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV">InstantiationErrorDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to create a <code><a href="../Classes/Style.html">Style</a></code> from a JSON source.</p>
<a class="slightly-smaller" href="../Classes/JsonStyleFactory/InstantiationErrorDetails.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct InstantiationErrorDetails</code></pre>
<pre><code>extension JsonStyleFactory.InstantiationErrorDetails : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createFromString(_:)"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ">createFromString(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of Style from a JSON string.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/JsonStyleFactory.html#/s:7heresdk16JsonStyleFactoryC18InstantiationErrora">JsonStyleFactory.InstantiationError</a></code> Indicates failure to create <code><a href="../Classes/Style.html">Style</a></code> from JSON string.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func createFromString(_ styleString: String) throws -&gt; Style</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>styleString</em>
</code>
</td>
<td>
<div>
<p>JSON style string.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Style instance.</p>
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
