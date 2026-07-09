---
title: "IsolineOptions.Calculation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IsolineOptions.Calculation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.IsolineOptions.Calculation</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">IsolineOptions.Calculation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Specifies isoline parameters.
 Setting at least one limit to <a href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#rangeValues"><code>rangeValues</code></a> is mandatory or the calculation will fail.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#isolineCalculationMode">isolineCalculationMode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies how isoline calculation is optimized.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#isolineDirection">isolineDirection</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Specifies if calculations will be from or to a specific point.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#maxPoints">maxPoints</a></code></div>
<div className="col-last even-row-color">
<div className="block">Limits the number of points in the resulting isoline polygon.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#rangeType">rangeType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Specifies the range of values to be included in the isoline.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#rangeValues">rangeValues</a></code></div>
<div className="col-last even-row-color">
<div className="block">A list of ranges.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues)</code></div>
<div className="col-last even-row-color"> </div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode)</code></div>
<div className="col-last odd-row-color"> </div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> maxPoints,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</code></div>
<div className="col-last even-row-color"> </div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions-calculation#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)">Calculation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</code></div>
<div className="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="rangeType">
<h3>rangeType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></span> <span className="element-name">rangeType</span></div>
<div className="block"><p>Specifies the range of values to be included in the isoline.</p></div>
</section>
</li>
<li>
<section className="detail" id="rangeValues">
<h3>rangeValues</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">rangeValues</span></div>
<div className="block"><p>A list of ranges. The unit is defined by the type parameter.
 Each range defines the maximum allowed value to reach a destination.
 For each value an <a href="sdk-for-android-navigate-com-here-sdk-routing-isoline" title="class in com.here.sdk.routing"><code>Isoline</code></a> is calculated indicating the reachable area.
 If empty, <a href="sdk-for-android-navigate-com-here-sdk-routing-isolineoptions" title="class in com.here.sdk.routing"><code>IsolineOptions</code></a> object is considered invalid.</p></div>
</section>
</li>
<li>
<section className="detail" id="isolineCalculationMode">
<h3>isolineCalculationMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a></span> <span className="element-name">isolineCalculationMode</span></div>
<div className="block"><p>Specifies how isoline calculation is optimized.
 The default waypoint type is <a href="sdk-for-android-navigate-isolinecalculationmode#BALANCED"><code>IsolineCalculationMode.BALANCED</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxPoints">
<h3>maxPoints</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">maxPoints</span></div>
<div className="block"><p>Limits the number of points in the resulting isoline polygon. If the
 isoline consists of multiple polygons, the sum of points from all
 polygons is considered. Note that this parameter does not affect the calculation,
 but the shape of the polygon. Look at <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing"><code>IsolineCalculationMode</code></a> parameter
 to optimize performance.
 A higher value will result in a more accurate polygon shape. Rendering a polygon
 with a high number of points can negatively impact rendering performance.
 The minimum allowed value is 30, lower values will be ignored.</p></div>
</section>
</li>
<li>
<section className="detail" id="isolineDirection">
<h3>isolineDirection</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a></span> <span className="element-name">isolineDirection</span></div>
<div className="block"><p>Specifies if calculations will be from or to a specific point.
 The default isoline direction is <a href="sdk-for-android-navigate-routeplacedirection#DEPARTURE"><code>RoutePlaceDirection.DEPARTURE</code></a>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List)">
<h3>Calculation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Calculation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)">
<h3>Calculation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Calculation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
<dd><code>isolineDirection</code> - <p>The isoline direction.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)">
<h3>Calculation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Calculation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>The range type.</p></dd>
<dd><code>rangeValues</code> - <p>Range values.</p></dd>
<dd><code>isolineCalculationMode</code> - <p>The isoline calculation mode.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)">
<h3>Calculation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Calculation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt; rangeValues,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a> isolineCalculationMode,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> maxPoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a> isolineDirection)</span></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
