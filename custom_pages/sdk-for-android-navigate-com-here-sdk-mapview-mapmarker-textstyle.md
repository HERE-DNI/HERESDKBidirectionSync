---
title: "MapMarker.TextStyle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMarker.TextStyle.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapMarker.TextStyle</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapMarker.TextStyle</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a> instance.</div>
</div>
<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents text placement with respect to the icon of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle#%3Cinit%3E()">TextStyle</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a default set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> that consists of
 the following values:
 
 Text size: 18 pixels
 Text color: opaque white
 Text outline size: 0 pixels
 Text outline color: opaque black
 Text placement: <a href="sdk-for-android-navigate-mapmarker-textstyle-placement#BOTTOM"><code>MapMarker.TextStyle.Placement.BOTTOM</code></a>
</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)">TextStyle</a><wbr/>(double textSize,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)">TextStyle</a><wbr/>(double textSize,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>TextStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TextStyle</span>()</div>
<div className="block"><p>Creates a default set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> that consists of
 the following values:
 <ul>
<li>Text size: 18 pixels</li>
<li>Text color: opaque white</li>
<li>Text outline size: 0 pixels</li>
<li>Text outline color: opaque black</li>
<li>Text placement: <a href="sdk-for-android-navigate-mapmarker-textstyle-placement#BOTTOM"><code>MapMarker.TextStyle.Placement.BOTTOM</code></a></li>
</ul>
Once the resulting <code>TextStyle</code> is applied to a <code>MapMarker</code>, its text will be centered over its
 image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)">
<h3>TextStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TextStyle</span><wbr/><span className="parameters">(double textSize,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements)</span>
          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></span></div>
<div className="block"><p>Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.
 List of placements is used to specify allowed placement of text relative to the icon.
 When marker overlapping is allowed as set by <a href="sdk-for-android-navigate-mapmarker#setOverlapAllowed(boolean)"><code>MapMarker.setOverlapAllowed(boolean)</code></a>,
 only first placement element is considered.
 Otherwise the placement value is chosen so that the text does not overlap
 with other <code>MapMarker</code> instances.
 Placement values are prioritized according
 to the order in which they appear in the list. Lists with duplicate entries
 as well as empty lists are not supported.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>textSize</code> - <p>The size of the text in pixels.
     Only positive values are supported.</p></dd>
<dd><code>textColor</code> - <p>The text color.</p></dd>
<dd><code>textOutlineSize</code> - <p>The size of the text outline in pixels.
     Only non-negative values are supported.</p></dd>
<dd><code>textOutlineColor</code> - <p>The color of the text outline.</p></dd>
<dd><code>placements</code> - <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)">
<h3>TextStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TextStyle</span><wbr/><span className="parameters">(double textSize,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName)</span>
          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></span></div>
<div className="block"><p>Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 List of placements is used to specify allowed placement of text relative to the icon.
 When marker overlapping is allowed as set by <a href="sdk-for-android-navigate-mapmarker#setOverlapAllowed(boolean)"><code>MapMarker.setOverlapAllowed(boolean)</code></a>,
 only first placement element is considered.
 Otherwise the placement value is chosen so that the text does not overlap
 with other <code>MapMarker</code> instances.
 Placement values are prioritized according
 to the order in which they appear in the list. Lists with duplicate entries
 as well as empty lists are not supported.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>textSize</code> - <p>The size of the text in pixels.
     Only positive values are supported.</p></dd>
<dd><code>textColor</code> - <p>The text color.</p></dd>
<dd><code>textOutlineSize</code> - <p>The size of the text outline in pixels.
     Only non-negative values are supported.</p></dd>
<dd><code>textOutlineColor</code> - <p>The color of the text outline.</p></dd>
<dd><code>placements</code> - <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
<dd><code>fontName</code> - <p>Font name, registered with <code>AssetsManager.registerFont</code>.
     If empty string is provided, a default font will be used.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
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
<section className="detail" id="getFontName()">
<h3>getFontName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getFontName</span>()</div>
<div className="block"><p>Gets the font name.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The font used in the text style.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTextSize()">
<h3>getTextSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getTextSize</span>()</div>
<div className="block"><p>Gets the text size in pixels.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The text size in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTextColor()">
<h3>getTextColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getTextColor</span>()</div>
<div className="block"><p>Gets the text color.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The text color.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTextOutlineSize()">
<h3>getTextOutlineSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getTextOutlineSize</span>()</div>
<div className="block"><p>Gets the text outline size in pixels.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The text outline size in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTextOutlineColor()">
<h3>getTextOutlineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getTextOutlineColor</span>()</div>
<div className="block"><p>Gets the text outline color.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The text outline color.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPlacements()">
<h3>getPlacements</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker-textstyle-placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt;</span> <span className="element-name">getPlacements</span>()</div>
<div className="block"><p>Gets the possible text placements relative to the icon of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of possible text placements relative to the icon of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
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
