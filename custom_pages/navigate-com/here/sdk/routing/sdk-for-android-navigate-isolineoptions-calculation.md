---
title: "IsolineOptions.Calculation (API Reference)"
slug: "sdk-for-android-navigate-isolineoptions-calculation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IsolineOptions.Calculation.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.IsolineOptions.Calculation</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">IsolineOptions.Calculation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Specifies isoline parameters.
 Setting at least one limit to <a href="#rangeValues"><code>rangeValues</code></a> is mandatory or the calculation will fail.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isolineCalculationMode">isolineCalculationMode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies how isoline calculation is optimized.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isolineDirection">isolineDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies if calculations will be from or to a specific point.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#maxPoints">maxPoints</a></code></div>
<div class="col-last even-row-color">
<div class="block">Limits the number of points in the resulting isoline polygon.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#rangeType">rangeType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the range of values to be included in the isoline.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#rangeValues">rangeValues</a></code></div>
<div class="col-last even-row-color">
<div class="block">A list of ranges.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> maxPoints,
 <a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="rangeType">
<h3>rangeType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></span> <span class="element-name">rangeType</span></div>
<div class="block"><p>Specifies the range of values to be included in the isoline.</p></div>
</section>
</li>
<li>
<section class="detail" id="rangeValues">
<h3>rangeValues</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">rangeValues</span></div>
<div class="block"><p>A list of ranges. The unit is defined by the type parameter.
 Each range defines the maximum allowed value to reach a destination.
 For each value an <a href="sdk-for-android-navigate-isoline" title="class in com.here.sdk.routing"><code>Isoline</code></a> is calculated indicating the reachable area.
 If empty, <a href="sdk-for-android-navigate-isolineoptions" title="class in com.here.sdk.routing"><code>IsolineOptions</code></a> object is considered invalid.</p></div>
</section>
</li>
<li>
<section class="detail" id="isolineCalculationMode">
<h3>isolineCalculationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a></span> <span class="element-name">isolineCalculationMode</span></div>
<div class="block"><p>Specifies how isoline calculation is optimized.
 The default waypoint type is <a href="sdk-for-android-navigate-isolinecalculationmode#BALANCED"><code>IsolineCalculationMode.BALANCED</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxPoints">
<h3>maxPoints</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxPoints</span></div>
<div class="block"><p>Limits the number of points in the resulting isoline polygon. If the
 isoline consists of multiple polygons, the sum of points from all
 polygons is considered. Note that this parameter does not affect the calculation,
 but the shape of the polygon. Look at <a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing"><code>IsolineCalculationMode</code></a> parameter
 to optimize performance.
 A higher value will result in a more accurate polygon shape. Rendering a polygon
 with a high number of points can negatively impact rendering performance.
 The minimum allowed value is 30, lower values will be ignored.</p></div>
</section>
</li>
<li>
<section class="detail" id="isolineDirection">
<h3>isolineDirection</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a></span> <span class="element-name">isolineDirection</span></div>
<div class="block"><p>Specifies if calculations will be from or to a specific point.
 The default isoline direction is <a href="sdk-for-android-navigate-routeplacedirection#DEPARTURE"><code>RoutePlaceDirection.DEPARTURE</code></a>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List)">
<h3>Calculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Calculation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)">
<h3>Calculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Calculation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
<dd><code>isolineDirection</code> - <p>The isoline direction.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)">
<h3>Calculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Calculation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
<dd><code>isolineCalculationMode</code> - <p>The isoline calculation mode.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)">
<h3>Calculation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Calculation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> maxPoints,
 @NonNull
 <a href="sdk-for-android-navigate-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
<dd><code>isolineCalculationMode</code> - <p>The isoline calculation mode.</p></dd>
<dd><code>maxPoints</code> - <p>The max points number.</p></dd>
<dd><code>isolineDirection</code> - <p>The isoline direction.</p></dd>
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
