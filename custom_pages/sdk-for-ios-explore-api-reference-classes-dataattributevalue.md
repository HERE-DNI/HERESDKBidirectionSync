---
title: "DataAttributeValue Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-dataattributevalue"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- DataAttributeValue.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributeValue"></a>
<a title="DataAttributeValue Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DataAttributeValue Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class DataAttributeValue</code></pre>
<pre><code>extension DataAttributeValue: NativeBase</code></pre>
<pre><code>extension DataAttributeValue: Hashable</code></pre>
</div>
</div>
<p>Encapsulates a data attribute value.
Supports basic types and arrays of basic types.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueCyACSScfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSScfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a string data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: String)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACs5Int64Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACs5Int64Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a 64-bit integer data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: Int64)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACSfcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSfcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a single precision floating decimal data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: Float)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACSdcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSdcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a double precision floating decimal data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: Double)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACSbcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSbcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a boolean data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: Bool)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACSo7UIColorCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSo7UIColorCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a color data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: UIColor)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueCyACSayACGcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueCyACSayACGcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an aggregated data attribute value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ value: [DataAttributeValue])</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
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
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ValueType"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO">ValueType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supported types of the data attribute values.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-dataattributevalue-valuetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum ValueType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC7getTypeAC0dF0OyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getType()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC7getTypeAC0dF0OyF">getType()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the type of the value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getType() -&gt; DataAttributeValue.ValueType</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The type of the value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC9getStringSSSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getString()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC9getStringSSSgyF">getString()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the string value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getString() -&gt; String?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC8getInt64s0F0VSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInt64()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC8getInt64s0F0VSgyF">getInt64()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets 64-bits integer value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getInt64() -&gt; Int64?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC8getFloatSfSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getFloat()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC8getFloatSfSgyF">getFloat()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the single precision floating decimal value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getFloat() -&gt; Float?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC9getDoubleSdSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDouble()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC9getDoubleSdSgyF">getDouble()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the double precision floating decimal value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getDouble() -&gt; Double?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC10getBooleanSbSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBoolean()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC10getBooleanSbSgyF">getBoolean()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the boolean value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getBoolean() -&gt; Bool?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC8getColorSo7UIColorCSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getColor()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC8getColorSo7UIColorCSgyF">getColor()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the color value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getColor() -&gt; UIColor?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC8getArraySayACGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getArray()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC8getArraySayACGSgyF">getArray()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the array value or <code>nil</code> if the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getArray() -&gt; [DataAttributeValue]?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC11getAsStringSSyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAsString()"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC11getAsStringSSyF">getAsString()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a string representation of the contained value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getAsString() -&gt; String</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
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
