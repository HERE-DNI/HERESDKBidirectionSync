---
title: "AssetsManager (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-assetsmanager"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AssetsManager.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.AssetsManager</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AssetsManager</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Assets manager interface. Can be used to make assets available to the SDK.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-assetsmanager#%3Cinit%3E(com.here.sdk.mapview.MapContext)">AssetsManager</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of AssetsManager.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext)">
<h3>AssetsManager</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AssetsManager</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context)</span></div>
<div className="block"><p>Creates an instance of AssetsManager.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>MapContext to which the assets belong.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="registerFont(java.lang.String,java.lang.String)">
<h3>registerFont</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">registerFont</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontPath)</span></div>
<div className="block"><p>Registers a font under a font name.
 After registration, the font name can be used in
 <ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> with <code>ImageFormat.SVG</code>.</li>
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a></li>
</ul>
Repeated registration with the same font name is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>fontName</code> - <p>A font name.</p></dd>
<dd><code>fontPath</code> - <p>A font file path. TTF, OTF and WOFF formats are supported.
     Can be an asset file path or an absolute file path.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="registerFontWithFallback(java.lang.String,java.lang.String,java.util.List)">
<h3>registerFontWithFallback</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">registerFontWithFallback</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontPath,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fallbackFontFilePaths)</span></div>
<div className="block"><p>Registers a font set under a font name.
 After registration, the font name can be used in
 <ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> with <code>ImageFormat.SVG</code>.</li>
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a></li>
</ul>
Repeated registration with the same font name is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>fontName</code> - <p>A font name.</p></dd>
<dd><code>fontPath</code> - <p>A font file path. TTF, OTF and WOFF formats are supported.
     Can be an asset file path or an absolute file path.</p></dd>
<dd><code>fallbackFontFilePaths</code> - <p>Additional font files are intended to be used if main font
     does not contain required character symbol and shall be sorted starting from most useful.</p></dd>
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
