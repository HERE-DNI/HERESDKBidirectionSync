---
title: "RoadSign (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadsign"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.RoadSign → com.here.sdk.navigation.RoadSign

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoadSign</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Describes a road sign. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">`GeneralWarningRoadSignType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#generalWarningType" class="member-name-link"><code>generalWarningType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies the general warning to which the road sign belongs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#isPrioritySign" class="member-name-link"><code>isPrioritySign</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Flag indicating if the road sign is a priority sign.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedDuration" class="member-name-link"><code>localizedDuration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional length information during which the warning is applicable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedPreWarning" class="member-name-link"><code>localizedPreWarning</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional pre-warning in terms of distance, of the upcoming warning or regulation.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedSignValue" class="member-name-link"><code>localizedSignValue</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">`LocalizedText`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#localizedValidityTime" class="member-name-link"><code>localizedValidityTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#offsetInMeters" class="member-name-link"><code>offsetInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The offset in meters from the beginning of the segment to the location of the road sign in positive direction.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">`RoadSignCategory`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#roadSignCategory" class="member-name-link"><code>roadSignCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The main category to which the road sign belongs.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">`RoadSignType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#roadSignType" class="member-name-link"><code>roadSignType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Type of the road sign.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">`TravelDirection`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#travelDirection" class="member-name-link"><code>travelDirection</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Segment direction which the road sign is applied.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">`RoadSignVehicleType`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#vehicleTypes" class="member-name-link"><code>vehicleTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies a list of vehicle types for which the road sign is applicable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">`WeatherType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign#weatherType" class="member-name-link"><code>weatherType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies the weather type for which the sign is applicable.

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

      RoadSign (int offsetInMeters, TravelDirection travelDirection, RoadSignType roadSignType, RoadSignCategory roadSignCategory,
       boolean isPrioritySign, GeneralWarningRoadSignType generalWarningType, List < RoadSignVehicleType > vehicleTypes, WeatherType weatherType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance with default values.

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

  - <div id="sdk-for-android-navigate-offsetInMeters" class="section detail">

    ### offsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">offsetInMeters</span>

    </div>

    <div class="block">

    The offset in meters from the beginning of the segment to the location of the road sign in positive direction.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-travelDirection" class="section detail">

    ### travelDirection

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span class="element-name">travelDirection</span>

    </div>

    <div class="block">

    Segment direction which the road sign is applied.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-roadSignType" class="section detail">

    ### roadSignType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">roadSignType</span>

    </div>

    <div class="block">

    Type of the road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-roadSignCategory" class="section detail">

    ### roadSignCategory

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span class="element-name">roadSignCategory</span>

    </div>

    <div class="block">

    The main category to which the road sign belongs.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isPrioritySign" class="section detail">

    ### isPrioritySign

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrioritySign</span>

    </div>

    <div class="block">

    Flag indicating if the road sign is a priority sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-generalWarningType" class="section detail">

    ### generalWarningType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span class="element-name">generalWarningType</span>

    </div>

    <div class="block">

    Specifies the general warning to which the road sign belongs.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-vehicleTypes" class="section detail">

    ### vehicleTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>\></span> <span class="element-name">vehicleTypes</span>

    </div>

    <div class="block">

    Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-weatherType" class="section detail">

    ### weatherType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weatherType</span>

    </div>

    <div class="block">

    Specifies the weather type for which the sign is applicable. If weather type is WeatherType.UNKNOWN , the sign is actual for all weather types.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-localizedSignValue" class="section detail">

    ### localizedSignValue

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedSignValue</span>

    </div>

    <div class="block">

    Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-localizedPreWarning" class="section detail">

    ### localizedPreWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedPreWarning</span>

    </div>

    <div class="block">

    Optional pre-warning in terms of distance, of the upcoming warning or regulation. The pre-warning information is given as printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-localizedDuration" class="section detail">

    ### localizedDuration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedDuration</span>

    </div>

    <div class="block">

    Optional length information during which the warning is applicable. Usually, this information is shown on a separate shield below the main shield. For example, a sign may warn on playing children for a length of 100 m, starting from the location of the warning sign. The length information (most likely with units) is given as printed on the local road sign.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-localizedValidityTime" class="section detail">

    ### localizedValidityTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedValidityTime</span>

    </div>

    <div class="block">

    Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable. The time information is given as printed on the local road sign.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-int-com-here-sdk-routing-TravelDirection-com-here-sdk-navigation-RoadSignType-com-here-sdk-navigation-RoadSignCategory-boolean-com-here-sdk-navigation-GeneralWarningRoadSignType-java-util-List-com-here-sdk-navigation-WeatherType" class="section detail">

    ### RoadSign

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoadSign</span><wbr></wbr><span class="parameters">(int offsetInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> roadSignType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> roadSignCategory, boolean isPrioritySign, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>\> vehicleTypes, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType)</span>

    </div>

    <div class="block">

    Creates a new instance with default values.

    </div>

    Parameters:  
    `offsetInMeters` -

    The offset in meters from the beginning of the segment to the location of the road sign in positive direction.

    `travelDirection` -

    Segment direction which the road sign is applied.

    `roadSignType` -

    Type of the road sign.

    `roadSignCategory` -

    The main category to which the road sign belongs.

    `isPrioritySign` -

    Flag indicating if the road sign is a priority sign.

    `generalWarningType` -

    Specifies the general warning to which the road sign belongs.

    `vehicleTypes` -

    Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

    `weatherType` -

    Specifies the weather type for which the sign is applicable. If weather type is `WeatherType.UNKNOWN`, the sign is actual for all weather types.

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

