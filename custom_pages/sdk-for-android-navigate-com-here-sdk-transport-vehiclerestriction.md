---
title: "VehicleRestriction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-transport-package-summary">com.here.sdk.transport</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.transport.VehicleRestriction → com.here.sdk.transport.VehicleRestriction

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleRestriction</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a vehicle restriction. Any non null field adds more details to the restriction. A general truck restriction is represented with null values for fields restriction and hazmatRestriction . Note: This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#appliesToDelivery" class="member-name-link"><code>appliesToDelivery</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Flag indicating whether this restriction applies to delivery vehicles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#axleCount" class="member-name-link"><code>axleCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The axle count for which the current restriction applies.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#axleCountInGroup" class="member-name-link"><code>axleCountInGroup</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of axles in a group for which the current restriction applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterialrestriction" title="class in com.here.sdk.transport">`HazardousMaterialRestriction`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#hazmatRestriction" class="member-name-link"><code>hazmatRestriction</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Restriction on transport of hazardous materials and max allowed tunnel category.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">`SpecificRestriction`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#restriction" class="member-name-link"><code>restriction</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A SpecificRestriction defines what type of restriction applies (weight, height, etc.) and the range of allowed values.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-timerestriction" title="class in com.here.sdk.transport">`TimeRestriction`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#timeRestriction" class="member-name-link"><code>timeRestriction</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Restriction applies during specific time.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#trailerCount" class="member-name-link"><code>trailerCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of trailers for which the restriction applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">`TruckCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#truckCategory" class="member-name-link"><code>truckCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Restriction applies to a specific truck category.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">`WeatherType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#weather" class="member-name-link"><code>weather</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Type of weather in which restriction applies.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      VehicleRestriction ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an uncoditional general restriction.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      VehicleRestriction ( SpecificRestriction restriction)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an unconditional restriction.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-restriction" class="section detail">

    ### restriction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a></span> <span class="element-name">restriction</span>

    </div>

    <div class="block">

    A SpecificRestriction defines what type of restriction applies (weight, height, etc.) and the range of allowed values.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-hazmatRestriction" class="section detail">

    ### hazmatRestriction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterialrestriction" title="class in com.here.sdk.transport">HazardousMaterialRestriction</a></span> <span class="element-name">hazmatRestriction</span>

    </div>

    <div class="block">

    Restriction on transport of hazardous materials and max allowed tunnel category. For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks carrying flammable materials are not allowed to enter tunnels category D and E - (TunnelCategory.B and TunnelCategory.C allowed).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeRestriction" class="section detail">

    ### timeRestriction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-timerestriction" title="class in com.here.sdk.transport">TimeRestriction</a></span> <span class="element-name">timeRestriction</span>

    </div>

    <div class="block">

    Restriction applies during specific time.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-appliesToDelivery" class="section detail">

    ### appliesToDelivery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">appliesToDelivery</span>

    </div>

    <div class="block">

    Flag indicating whether this restriction applies to delivery vehicles. false means delivery is allowed into this restricted street. true means delivery is NOT allowed into this restricted street.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-weather" class="section detail">

    ### weather

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weather</span>

    </div>

    <div class="block">

    Type of weather in which restriction applies.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-truckCategory" class="section detail">

    ### truckCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span class="element-name">truckCategory</span>

    </div>

    <div class="block">

    Restriction applies to a specific truck category.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-trailerCount" class="section detail">

    ### trailerCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">trailerCount</span>

    </div>

    <div class="block">

    Number of trailers for which the restriction applies.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-axleCount" class="section detail">

    ### axleCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCount</span>

    </div>

    <div class="block">

    The axle count for which the current restriction applies. Can be used in conjunction with RestrictionType.WEIGHT_PER_AXLE_COUNT to specify restriction based on weight per number of axles. The axleCount considers total number of axles on the whole vehicle (truck + trailers). This can be used to limit the weight per axle for the whole truck. If axleCount is null, the restriction is general and applies regardless of axle count. If the upper limit of the axleCount range is 0 or null then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. When a user taps the icon, the allowed axleCount range can be retrieved directly from VehicleRestriction.axleCount . Examples: (2,2) → Restriction applies to vehicles with exactly 2 axles. (2,4) → Restriction applies to vehicles with 2, 3, or 4 axles. (2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2...∞)

    </div>

    </div>

  - <div id="sdk-for-android-navigate-axleCountInGroup" class="section detail">

    ### axleCountInGroup

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCountInGroup</span>

    </div>

    <div class="block">

    Number of axles in a group for which the current restriction applies. axleCountInGroup is a set of axles close together: single, tandem (2), triple (3), etc. Can be used in conjunction with RestrictionType.WEIGHT_PER_AXLE_GROUP to specify restriction based on weight per axle group. The axleCountInGroup considers number of axles in a specific axle group (usually rear axles on the truck or trailer). This can be used to limit weight for a tandem/triple rear axle group. If the upper limit of the axleCountInGroup range is 0 or null then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. Examples: (1,1) → Restriction applies to single axle group. (2,2) → Restriction applies to tandem axle group. (2,4) → Restriction applies to any axle group from 2 to 4 axles. (2,0) → Restriction applies to axle groups with 2 or more axles.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-transport-SpecificRestriction" class="section detail">

    ### VehicleRestriction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a> restriction)</span>

    </div>

    <div class="block">

    Creates an unconditional restriction.

    </div>

    Parameters:  
    `restriction` -

    A `SpecificRestriction` defines what type of restriction applies (weight, height, etc.) and the range of allowed values.

    </div>

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### VehicleRestriction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span>()

    </div>

    <div class="block">

    Creates an uncoditional general restriction.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

