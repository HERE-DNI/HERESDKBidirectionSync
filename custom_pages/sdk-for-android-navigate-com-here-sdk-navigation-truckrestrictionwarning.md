---
title: "TruckRestrictionWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.TruckRestrictionWarning → com.here.sdk.navigation.TruckRestrictionWarning

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TruckRestrictionWarning</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck or there can be a road ahead where the truck’s weight exceeds the permissible limit.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#axleCount" class="member-name-link"><code>axleCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The axle count for which the current restriction applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-dimensionrestriction" title="class in com.here.sdk.navigation">`DimensionRestriction`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#dimensionRestriction" class="member-name-link"><code>dimensionRestriction</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Vehicle dimension restrictions.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceInMeters" class="member-name-link"><code>distanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The distance from the current location to the restriction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">`DistanceType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceType" class="member-name-link"><code>distanceType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates if the specified truck restriction is ahead of the vehicle or has just passed by.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">`HazardousMaterial`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#hazardousMaterials" class="member-name-link"><code>hazardousMaterials</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of hazardous materials which are restricted on the road section for which the warning applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#id" class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Unique identifier for this specific truck restriction warning instance.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">`TimeRule`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#timeRule" class="member-name-link"><code>timeRule</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Time rule indicating the time periods for which the restriction applies.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">`IntegerRange`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#trailerCount" class="member-name-link"><code>trailerCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The trailer count for which the current restriction applies.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">`TruckRoadType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#truckRoadType" class="member-name-link"><code>truckRoadType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Truck road type restriction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">`TunnelCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#tunnelCategory" class="member-name-link"><code>tunnelCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Tunnel category.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-weightrestriction" title="class in com.here.sdk.navigation">`WeightRestriction`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#weightRestriction" class="member-name-link"><code>weightRestriction</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Weight restriction.

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

      TruckRestrictionWarning (double distanceInMeters, DistanceType distanceType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isGeneral ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Checks if this truck restriction warning is general.

  </div>

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

  - <div id="sdk-for-android-navigate-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Unique identifier for this specific truck restriction warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceInMeters" class="section detail">

    ### distanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceInMeters</span>

    </div>

    <div class="block">

    The distance from the current location to the restriction.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-weightRestriction" class="section detail">

    ### weightRestriction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weightrestriction" title="class in com.here.sdk.navigation">WeightRestriction</a></span> <span class="element-name">weightRestriction</span>

    </div>

    <div class="block">

    Weight restriction. It is null when there is no known weight restriction ahead.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-dimensionRestriction" class="section detail">

    ### dimensionRestriction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dimensionrestriction" title="class in com.here.sdk.navigation">DimensionRestriction</a></span> <span class="element-name">dimensionRestriction</span>

    </div>

    <div class="block">

    Vehicle dimension restrictions. It is null when there is no known dimension restriction ahead.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceType" class="section detail">

    ### distanceType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span>

    </div>

    <div class="block">

    Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then distanceInMeters is greater than 0.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-trailerCount" class="section detail">

    ### trailerCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">trailerCount</span>

    </div>

    <div class="block">

    The trailer count for which the current restriction applies. If the field is 'null' then the current restriction does not have a condition based on trailers count.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeRule" class="section detail">

    ### timeRule

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span>

    </div>

    <div class="block">

    Time rule indicating the time periods for which the restriction applies. If the field is 'null' then the restriction is applicable at anytime.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-truckRoadType" class="section detail">

    ### truckRoadType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a></span> <span class="element-name">truckRoadType</span>

    </div>

    <div class="block">

    Truck road type restriction.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-hazardousMaterials" class="section detail">

    ### hazardousMaterials

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>\></span> <span class="element-name">hazardousMaterials</span>

    </div>

    <div class="block">

    The list of hazardous materials which are restricted on the road section for which the warning applies.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-tunnelCategory" class="section detail">

    ### tunnelCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span class="element-name">tunnelCategory</span>

    </div>

    <div class="block">

    Tunnel category.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-axleCount" class="section detail">

    ### axleCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCount</span>

    </div>

    <div class="block">

    The axle count for which the current restriction applies. If this field is null , the restriction does not depend on axle count.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-com-here-sdk-navigation-DistanceType" class="section detail">

    ### TruckRestrictionWarning

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TruckRestrictionWarning</span><wbr></wbr><span class="parameters">(double distanceInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `distanceInMeters` -

    The distance from the current location to the restriction.

    `distanceType` -

    Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceInMeters">`distanceInMeters`</a> is greater than 0.

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

  - <div id="sdk-for-android-navigate-isGeneral" class="section detail">

    ### isGeneral

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isGeneral</span>()

    </div>

    <div class="block">

    Checks if this truck restriction warning is general. A general warning has no specific restriction conditions set. Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition. This method only checks that no specific conditions are set for the warning.

    </div>

    Returns:  
    `true` if all restriction fields are null or empty, `false` otherwise.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

