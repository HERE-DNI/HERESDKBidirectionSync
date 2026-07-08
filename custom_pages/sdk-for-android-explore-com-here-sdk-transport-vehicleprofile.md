---
title: "VehicleProfile (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-vehicleprofile"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.transport](sdk-for-android-explore-com-here-sdk-transport-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.transport.VehicleProfile → com.here.sdk.transport.VehicleProfile

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleProfile</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="deprecation-block">

<span class="deprecated-label">Deprecated.</span>

<div class="deprecation-comment">

Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.

</div>

</div>

<div class="block">

A vehicle profile describes the vehicle being used with the HSDK. The profile is planned to be used as single source of information describing the vehicle. Current modules that use this profile: Navigation: Tracking mode for truck related vehicle restrictions. Note: This is a beta release of this vehicle profile, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#axleCount" class="member-name-link"><code>axleCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Defines total number of axles in the vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#grossWeightInKilograms" class="member-name-link"><code>grossWeightInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Vehicle weight including trailers and shipped goods in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`HazardousMaterial`](sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial "enum class in com.here.sdk.transport")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#hazardousMaterials" class="member-name-link"><code>hazardousMaterials</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Specifies a list of hazardous materials shipped in the vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#heightInCentimeters" class="member-name-link"><code>heightInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Vehicle height in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#lengthInCentimeters" class="member-name-link"><code>lengthInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Vehicle length in centimeters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#trailerCount" class="member-name-link"><code>trailerCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Defines number of trailers attached to the vehicle.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TruckCategory`](sdk-for-android-explore-com-here-sdk-transport-truckcategory "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#truckCategory" class="member-name-link"><code>truckCategory</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Defines the truck category.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`TunnelCategory`](sdk-for-android-explore-com-here-sdk-transport-tunnelcategory "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#tunnelCategory" class="member-name-link"><code>tunnelCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Specifies the tunnel categories to restrict certain route links.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`VehicleType`](sdk-for-android-explore-com-here-sdk-transport-vehicletype "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#vehicleType" class="member-name-link"><code>vehicleType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Defines the vehicle type.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#weightPerAxleInKilograms" class="member-name-link"><code>weightPerAxleInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Vehicle weight per axle in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-transport-vehicleprofile#widthInCentimeters" class="member-name-link"><code>widthInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Vehicle width in centimeters.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      VehicleProfile ( VehicleType vehicleType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated.

  </div>

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated.

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

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-vehicleType" class="section detail">

    ### vehicleType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[VehicleType](sdk-for-android-explore-com-here-sdk-transport-vehicletype "enum class in com.here.sdk.transport")</span> <span class="element-name">vehicleType</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines the vehicle type.

    </div>

    </div>

  - <div id="sdk-for-android-explore-truckCategory" class="section detail">

    ### truckCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TruckCategory](sdk-for-android-explore-com-here-sdk-transport-truckcategory "enum class in com.here.sdk.transport")</span> <span class="element-name">truckCategory</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines the truck category. Only used when the vehicleType is VehicleType.TRUCK By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trailerCount" class="section detail">

    ### trailerCount

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">trailerCount</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. When not set, possible trailer count restrictions will not be taken into consideration for route calculation. By default, it is 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-hazardousMaterials" class="section detail">

    ### hazardousMaterials

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[HazardousMaterial](sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial "enum class in com.here.sdk.transport")\></span> <span class="element-name">hazardousMaterials</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies a list of hazardous materials shipped in the vehicle. Refer to HazardousMaterial for the available options.

    </div>

    </div>

  - <div id="sdk-for-android-explore-tunnelCategory" class="section detail">

    ### tunnelCategory

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TunnelCategory](sdk-for-android-explore-com-here-sdk-transport-tunnelcategory "enum class in com.here.sdk.transport")</span> <span class="element-name">tunnelCategory</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to TunnelCategory for the available options.

    </div>

    </div>

  - <div id="sdk-for-android-explore-axleCount" class="section detail">

    ### axleCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">axleCount</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. When not set, possible axle count restrictions will not be taken into consideration for route calculation. By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-grossWeightInKilograms" class="section detail">

    ### grossWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">grossWeightInKilograms</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle weight including trailers and shipped goods in kilograms. By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-heightInCentimeters" class="section detail">

    ### heightInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">heightInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-lengthInCentimeters" class="section detail">

    ### lengthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">lengthInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-widthInCentimeters" class="section detail">

    ### widthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">widthInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-weightPerAxleInKilograms" class="section detail">

    ### weightPerAxleInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">weightPerAxleInKilograms</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0. When not set, possible weight per axle restrictions will not be taken into consideration for route calculation. By default, it is not set.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-transport-VehicleType" class="section detail">

    ### VehicleProfile

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleProfile</span><wbr></wbr><span class="parameters">(@NonNull [VehicleType](sdk-for-android-explore-com-here-sdk-transport-vehicletype "enum class in com.here.sdk.transport") vehicleType)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `vehicleType` -

    Defines the vehicle type.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

