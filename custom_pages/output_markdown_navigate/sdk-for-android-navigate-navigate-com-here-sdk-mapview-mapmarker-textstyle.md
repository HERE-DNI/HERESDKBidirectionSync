---
title: "MapMarker.TextStyle (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-mapview-mapmarker-textstyle"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarker.TextStyle.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapMarker.TextStyle</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapMarker.TextStyle</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapmarker.textstyle.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapmarker.textstyle.instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create a <a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a> instance.</div>
</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a></code></div>
<div class="col-last even-row-color">
<div class="block">Represents text placement with respect to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TextStyle</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a default set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> that consists of
 the following values:
 
 Text size: 18 pixels
 Text color: opaque white
 Text outline size: 0 pixels
 Text outline color: opaque black
 Text placement: <a href="sdk-for-android-navigate-mapmarker.textstyle.placement#BOTTOM"><code>MapMarker.TextStyle.Placement.BOTTOM</code></a>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)">TextStyle</a><wbr/>(double textSize,
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)">TextStyle</a><wbr/>(double textSize,
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontName()">getFontName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the font name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPlacements()">getPlacements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the possible text placements relative to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextColor()">getTextColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text color.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextOutlineColor()">getTextOutlineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text outline color.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextOutlineSize()">getTextOutlineSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text outline size in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextSize()">getTextSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text size in pixels.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>TextStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextStyle</span>()</div>
<div class="block"><p>Creates a default set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> that consists of
 the following values:
 <ul>
<li>Text size: 18 pixels</li>
<li>Text color: opaque white</li>
<li>Text outline size: 0 pixels</li>
<li>Text outline color: opaque black</li>
<li>Text placement: <a href="sdk-for-android-navigate-mapmarker.textstyle.placement#BOTTOM"><code>MapMarker.TextStyle.Placement.BOTTOM</code></a></li>
</ul>
</p><p>Once the resulting <code>TextStyle</code> is applied to a <code>MapMarker</code>, its text will be centered over its
 image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)">
<h3>TextStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextStyle</span><wbr/><span class="parameters">(double textSize,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements)</span>
          throws <span class="exceptions"><a href="sdk-for-android-navigate-mapmarker.textstyle.instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></span></div>
<div class="block"><p>Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.
 </p><p>List of placements is used to specify allowed placement of text relative to the icon.
 When marker overlapping is allowed as set by <a href="sdk-for-android-navigate-mapmarker#setOverlapAllowed(boolean)"><code>MapMarker.setOverlapAllowed(boolean)</code></a>,
 only first placement element is considered.
 Otherwise the placement value is chosen so that the text does not overlap
 with other <code>MapMarker</code> instances.
 </p><p>Placement values are prioritized according
 to the order in which they appear in the list. Lists with duplicate entries
 as well as empty lists are not supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>textSize</code> - <p>The size of the text in pixels.
     Only positive values are supported.</p></dd>
<dd><code>textColor</code> - <p>The text color.</p></dd>
<dd><code>textOutlineSize</code> - <p>The size of the text outline in pixels.
     Only non-negative values are supported.</p></dd>
<dd><code>textOutlineColor</code> - <p>The color of the text outline.</p></dd>
<dd><code>placements</code> - <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapmarker.textstyle.instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)">
<h3>TextStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextStyle</span><wbr/><span class="parameters">(double textSize,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textColor,
 double textOutlineSize,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> textOutlineColor,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt; placements,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fontName)</span>
          throws <span class="exceptions"><a href="sdk-for-android-navigate-mapmarker.textstyle.instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></span></div>
<div class="block"><p>Creates a set of styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 </p><p>List of placements is used to specify allowed placement of text relative to the icon.
 When marker overlapping is allowed as set by <a href="sdk-for-android-navigate-mapmarker#setOverlapAllowed(boolean)"><code>MapMarker.setOverlapAllowed(boolean)</code></a>,
 only first placement element is considered.
 Otherwise the placement value is chosen so that the text does not overlap
 with other <code>MapMarker</code> instances.
 </p><p>Placement values are prioritized according
 to the order in which they appear in the list. Lists with duplicate entries
 as well as empty lists are not supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>textSize</code> - <p>The size of the text in pixels.
     Only positive values are supported.</p></dd>
<dd><code>textColor</code> - <p>The text color.</p></dd>
<dd><code>textOutlineSize</code> - <p>The size of the text outline in pixels.
     Only non-negative values are supported.</p></dd>
<dd><code>textOutlineColor</code> - <p>The color of the text outline.</p></dd>
<dd><code>placements</code> - <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
<dd><code>fontName</code> - <p>Font name, registered with <code>AssetsManager.registerFont</code>.
     If empty string is provided, a default font will be used.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapmarker.textstyle.instantiationexception" title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getFontName()">
<h3>getFontName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFontName</span>()</div>
<div class="block"><p>Gets the font name.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The font used in the text style.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextSize()">
<h3>getTextSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTextSize</span>()</div>
<div class="block"><p>Gets the text size in pixels.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The text size in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextColor()">
<h3>getTextColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getTextColor</span>()</div>
<div class="block"><p>Gets the text color.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The text color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextOutlineSize()">
<h3>getTextOutlineSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTextOutlineSize</span>()</div>
<div class="block"><p>Gets the text outline size in pixels.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The text outline size in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextOutlineColor()">
<h3>getTextOutlineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getTextOutlineColor</span>()</div>
<div class="block"><p>Gets the text outline color.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The text outline color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPlacements()">
<h3>getPlacements</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker.textstyle.placement" title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a>&gt;</span> <span class="element-name">getPlacements</span>()</div>
<div class="block"><p>Gets the possible text placements relative to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of possible text placements relative to the icon of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
