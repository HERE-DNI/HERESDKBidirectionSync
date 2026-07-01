---
title: "IsolineOptions.Calculation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.IsolineOptions.Calculation

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[IsolineOptions](sdk-for-android-explore-com-here-sdk-routing-isolineoptions "class in com.here.sdk.routing")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">IsolineOptions.Calculation</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Specifies isoline parameters. Setting at least one limit to rangeValues
is mandatory or the calculation will fail.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolinecalculationmode"
  title="enum class in com.here.sdk.routing"><code>IsolineCalculationMode</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation#isolineCalculationMode"
  class="member-name-link"><code>isolineCalculationMode</code></a></td>
  <td><div class="block">
  Specifies how isoline calculation is optimized.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplacedirection"
  title="enum class in com.here.sdk.routing"><code>RoutePlaceDirection</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation#isolineDirection"
  class="member-name-link"><code>isolineDirection</code></a></td>
  <td><div class="block">
  Specifies if calculations will be from or to a specific point.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation#maxPoints"
  class="member-name-link"><code>maxPoints</code></a></td>
  <td><div class="block">
  Limits the number of points in the resulting isoline polygon.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolinerangetype"
  title="enum class in com.here.sdk.routing"><code>IsolineRangeType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation#rangeType"
  class="member-name-link"><code>rangeType</code></a></td>
  <td><div class="block">
  Specifies the range of values to be included in the isoline.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation#rangeValues"
  class="member-name-link"><code>rangeValues</code></a></td>
  <td><div class="block">
  A list of ranges.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>Calculation(IsolineRangeType rangeType,
   List&lt;Integer&gt; rangeValues)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><pre><code>Calculation(IsolineRangeType rangeType,
   List&lt;Integer&gt; rangeValues,
   IsolineCalculationMode isolineCalculationMode)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><pre><code>Calculation(IsolineRangeType rangeType,
   List&lt;Integer&gt; rangeValues,
   IsolineCalculationMode isolineCalculationMode,
   Integer maxPoints,
   RoutePlaceDirection isolineDirection)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><pre><code>Calculation(IsolineRangeType rangeType,
   List&lt;Integer&gt; rangeValues,
   RoutePlaceDirection isolineDirection)</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="rangeType" class="section detail">

    ### rangeType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing")</span> <span class="element-name">rangeType</span>

    </div>

    <div class="block">

    Specifies the range of values to be included in the isoline.

    </div>

    </div>

  - <div id="rangeValues" class="section detail">

    ### rangeValues

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>></span> <span class="element-name">rangeValues</span>

    </div>

    <div class="block">

    A list of ranges. The unit is defined by the type parameter. Each
    range defines the maximum allowed value to reach a destination. For
    each value an Isoline is calculated indicating the reachable area.
    If empty, IsolineOptions object is considered invalid.

    </div>

    </div>

  - <div id="isolineCalculationMode" class="section detail">

    ### isolineCalculationMode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[IsolineCalculationMode](sdk-for-android-explore-com-here-sdk-routing-isolinecalculationmode "enum class in com.here.sdk.routing")</span> <span class="element-name">isolineCalculationMode</span>

    </div>

    <div class="block">

    Specifies how isoline calculation is optimized. The default waypoint
    type is IsolineCalculationMode.BALANCED .

    </div>

    </div>

  - <div id="maxPoints" class="section detail">

    ### maxPoints

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">maxPoints</span>

    </div>

    <div class="block">

    Limits the number of points in the resulting isoline polygon. If the
    isoline consists of multiple polygons, the sum of points from all
    polygons is considered. Note that this parameter does not affect the
    calculation, but the shape of the polygon. Look at
    IsolineCalculationMode parameter to optimize performance. A higher
    value will result in a more accurate polygon shape. Rendering a
    polygon with a high number of points can negatively impact rendering
    performance. The minimum allowed value is 30, lower values will be
    ignored.

    </div>

    </div>

  - <div id="isolineDirection" class="section detail">

    ### isolineDirection

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoutePlaceDirection](sdk-for-android-explore-com-here-sdk-routing-routeplacedirection "enum class in com.here.sdk.routing")</span> <span class="element-name">isolineDirection</span>

    </div>

    <div class="block">

    Specifies if calculations will be from or to a specific point. The
    default isoline direction is RoutePlaceDirection.DEPARTURE .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.IsolineRangeType,java.util.List)"
    class="section detail">

    ### Calculation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Calculation</span><span class="parameters">(@NonNull
    [IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing") rangeType,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> rangeValues)</span>

    </div>

    Parameters:  
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.RoutePlaceDirection)"
    class="section detail">

    ### Calculation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Calculation</span><span class="parameters">(@NonNull
    [IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing") rangeType,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> rangeValues,
    @NonNull
    [RoutePlaceDirection](sdk-for-android-explore-com-here-sdk-routing-routeplacedirection "enum class in com.here.sdk.routing") isolineDirection)</span>

    </div>

    Parameters:  
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineDirection` -

    The isoline direction.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode)"
    class="section detail">

    ### Calculation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Calculation</span><span class="parameters">(@NonNull
    [IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing") rangeType,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> rangeValues,
    @NonNull
    [IsolineCalculationMode](sdk-for-android-explore-com-here-sdk-routing-isolinecalculationmode "enum class in com.here.sdk.routing") isolineCalculationMode)</span>

    </div>

    Parameters:  
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineCalculationMode` -

    The isoline calculation mode.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineRangeType,java.util.List,com.here.sdk.routing.IsolineCalculationMode,java.lang.Integer,com.here.sdk.routing.RoutePlaceDirection)"
    class="section detail">

    ### Calculation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Calculation</span><span class="parameters">(@NonNull
    [IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing") rangeType,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> rangeValues,
    @NonNull
    [IsolineCalculationMode](sdk-for-android-explore-com-here-sdk-routing-isolinecalculationmode "enum class in com.here.sdk.routing") isolineCalculationMode,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a> maxPoints,
    @NonNull
    [RoutePlaceDirection](sdk-for-android-explore-com-here-sdk-routing-routeplacedirection "enum class in com.here.sdk.routing") isolineDirection)</span>

    </div>

    Parameters:  
    `rangeType` -

    The range type.

    `rangeValues` -

    Range values.

    `isolineCalculationMode` -

    The isoline calculation mode.

    `maxPoints` -

    The max points number.

    `isolineDirection` -

    The isoline direction.

    </div>

  </div>

</div>

