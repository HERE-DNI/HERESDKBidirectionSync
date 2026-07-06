---
title: "VehicleSpecification (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-vehiclespecification"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.transport](sdk-for-android-explore-com-here-sdk-transport-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.transport.VehicleSpecification

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">VehicleSpecification</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains vehicle related attributes. Examples: Dimensions, weight, axle
count. Only the fields that are set are considered for restriction
handling.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-busbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.BusBuilder</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a bus.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-carbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.CarBuilder</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a car.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-privatebusbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.PrivateBusBuilder</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a private bus.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-scooterbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.ScooterBuilder</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a scooter.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-taxibuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.TaxiBuilder</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a taxi.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification-truckbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>VehicleSpecification.TruckBuilder</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  This class constructs a VehicleSpecification for a truck.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#axleCount"
  class="member-name-link"><code>axleCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines total number of axles in the vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#currentWeightInKilograms"
  class="member-name-link"><code>currentWeightInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Current truck weight, including trailers and shipped goods currently
  loaded, specified in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#emptyWeightInKilograms"
  class="member-name-link"><code>emptyWeightInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Empty weight of the vehicle without any load, excluding trailers,
  specified in kilograms.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#engineSizeInCubicCentimeters"
  class="member-name-link"><code>engineSizeInCubicCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Engine size of the scooter in cubic centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#grossWeightInKilograms"
  class="member-name-link"><code>grossWeightInKilograms</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Gross truck weight, including trailers and shipped goods when loaded
  at capacity, specified in kilograms.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`HazardousMaterial`](sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial "enum class in com.here.sdk.transport")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#hazardousMaterials"
  class="member-name-link"><code>hazardousMaterials</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies a list of hazardous materials shipped in the vehicle.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#heightInCentimeters"
  class="member-name-link"><code>heightInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Vehicle height in centimeters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#isCommercial"
  class="member-name-link"><code>isCommercial</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies whether the vehicle is a commercial or a non-commercial
  vehicle.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#isTruckLight"
  class="member-name-link"><code>isTruckLight</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag indicating whether the truck is light enough to be classified
  more as a car than a truck in Japan.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#kingpinToRearAxleDistanceInCentimeters"
  class="member-name-link"><code>kingpinToRearAxleDistanceInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the kingpin to rear axle distance, in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#lastCharacterOfLicensePlate"
  class="member-name-link"><code>lastCharacterOfLicensePlate</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Last character of license plate in String format.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#lengthInCentimeters"
  class="member-name-link"><code>lengthInCentimeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Vehicle length in centimeters.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#occupancy"
  class="member-name-link"><code>occupancy</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies the number of occupants in the vehicle, including driver,
  can affect the vehicle's ability to use HOV/carpool restricted lanes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#payloadCapacityInKilograms"
  class="member-name-link"><code>payloadCapacityInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Allowed payload capacity, including trailers, specified in kilograms.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#tiresCount"
  class="member-name-link"><code>tiresCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The total number of tires the vehicle has, i.e., the tires on the base
  vehicle and any attached trailers.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerAxleCount"
  class="member-name-link"><code>trailerAxleCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines total number of axles across all the trailers attached to the
  vehicle.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#trailerCount"
  class="member-name-link"><code>trailerCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines number of trailers attached to the vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`TruckCategory`](sdk-for-android-explore-com-here-sdk-transport-truckcategory "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckCategory"
  class="member-name-link"><code>truckCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the truck category.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TruckType`](sdk-for-android-explore-com-here-sdk-transport-trucktype "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#truckType"
  class="member-name-link"><code>truckType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.27.0.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`TunnelCategory`](sdk-for-android-explore-com-here-sdk-transport-tunnelcategory "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#tunnelCategory"
  class="member-name-link"><code>tunnelCategory</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies the tunnel categories to restrict certain route links.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`WeightPerAxleGroup`](sdk-for-android-explore-com-here-sdk-transport-weightperaxlegroup "class in com.here.sdk.transport")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleGroup"
  class="member-name-link"><code>weightPerAxleGroup</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Allows specification of axle weights in a more fine-grained way than
  weightPerAxleInKilograms .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#weightPerAxleInKilograms"
  class="member-name-link"><code>weightPerAxleInKilograms</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Heaviest weight per axle, regardless of axle type or axle group.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification#widthInCentimeters"
  class="member-name-link"><code>widthInCentimeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Vehicle width in centimeters.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      VehicleSpecification()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-heightInCentimeters"
    class="section detail">

    ### heightInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">heightInCentimeters</span>

    </div>

    <div class="block">

    Vehicle height in centimeters. The provided value must be in the
    range \[0, 5000\]. By default, it is not set. Note: Supported in
    TransportMode.TRUCK , TransportMode.BUS , TransportMode.PRIVATE_BUS
    , TransportMode.CAR (Beta), TransportMode.TAXI (Beta) transport
    modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-widthInCentimeters"
    class="section detail">

    ### widthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">widthInCentimeters</span>

    </div>

    <div class="block">

    Vehicle width in centimeters. The provided value must be in the
    range \[0, 5000\]. By default, it is not set. Note: Supported in
    TransportMode.TRUCK , TransportMode.BUS , TransportMode.PRIVATE_BUS
    , TransportMode.CAR (Beta), TransportMode.TAXI (Beta) transport
    modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-lengthInCentimeters"
    class="section detail">

    ### lengthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">lengthInCentimeters</span>

    </div>

    <div class="block">

    Vehicle length in centimeters. The provided value must be in the
    range \[0, 30000\]. By default, it is not set. Note: Supported in
    TransportMode.TRUCK , TransportMode.BUS , TransportMode.PRIVATE_BUS
    , TransportMode.CAR (Beta), TransportMode.TAXI (Beta) transport
    modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-axleCount" class="section detail">

    ### axleCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">axleCount</span>

    </div>

    <div class="block">

    Defines total number of axles in the vehicle. The provided value
    must be greater than or equal to 2. By default, it is not set. Route
    calculation: When not set, possible axle count restrictions will not
    be taken into consideration. Rendering: When set, truck restriction
    icons for an axle count greater than axleCount will not be
    displayed. When specifying trailerAxleCount , then axleCount is
    required and must be greater than trailerAxleCount . Note: Supported
    in TransportMode.TRUCK , TransportMode.BUS ,
    TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trailerCount"
    class="section detail">

    ### trailerCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerCount</span>

    </div>

    <div class="block">

    Defines number of trailers attached to the vehicle. The provided
    value must be in the range \[0, 255\]. By default, it is not set.
    When specifying trailerAxleCount , then trailerCount is required and
    must be greater than 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-truckType" class="section detail">

    ### truckType

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a> @NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TruckType](sdk-for-android-explore-com-here-sdk-transport-trucktype "enum class in com.here.sdk.transport")</span> <span class="element-name">truckType</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Use `VehicleSpecification.truckCategory`
    instead.

    </div>

    </div>

    <div class="block">

    Will be replaced with truckCategory when the TruckSpecification will
    be replaced by VehicleSpecification . Defines the type of truck.
    Defaults to TruckType.STRAIGHT . Rendering sdk.mapview.TruckProfile
    : truckType is ignored and has no effect.

    </div>

    </div>

  - <div id="sdk-for-android-explore-truckCategory"
    class="section detail">

    ### truckCategory

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TruckCategory](sdk-for-android-explore-com-here-sdk-transport-truckcategory "enum class in com.here.sdk.transport")</span> <span class="element-name">truckCategory</span>

    </div>

    <div class="block">

    Defines the truck category. By default, it is not set. Rendering:
    truckCategory is ignored and has no effect.

    </div>

    </div>

  - <div id="sdk-for-android-explore-isTruckLight"
    class="section detail">

    ### isTruckLight

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTruckLight</span>

    </div>

    <div class="block">

    A flag indicating whether the truck is light enough to be classified
    more as a car than a truck in Japan. The flag should not be set to
    true in other countries than Japan. Defaults to false . A light
    truck exempts from many legal restrictions for normal trucks in
    Japan, for example, which streets the vehicle can access, which
    access restrictions apply, and which speed limits are applicable.
    Restrictions related to the dimensions of the truck, or its cargo
    may still apply and setting this flag will not always overwrite
    these settings. Make sure to not exceed the specifications that
    classify a truck as light. In Japan, for light trucks the same
    restrictions apply as for cars. Therefore, when the flag is set to
    true , you will get, for example, the same speed limits as for cars.
    Make sure to set the flag only to true , when a vehicle matches the
    classification for light trucks according to the vehicle regulations
    in Japan. When on MapContentSettings , then this flag will be
    ignored and has no effect. Notes: This flag and the concept of light
    trucks are supported only in Japan as beta and are considered to be
    experimental in other regions. Therefore, for now, it is recommended
    to use this flag only in Japan. Note that this is a beta release of
    this feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process. Supported only in TransportMode.TRUCK transport mode.

    </div>

    </div>

  - <div id="sdk-for-android-explore-payloadCapacityInKilograms"
    class="section detail">

    ### payloadCapacityInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">payloadCapacityInKilograms</span>

    </div>

    <div class="block">

    Allowed payload capacity, including trailers, specified in
    kilograms. The provided value must be greater then or equal to 0. By
    default, it is not set. Note: Supported in TransportMode.TRUCK ,
    TransportMode.CAR (Beta), TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trailerAxleCount"
    class="section detail">

    ### trailerAxleCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerAxleCount</span>

    </div>

    <div class="block">

    Defines total number of axles across all the trailers attached to
    the vehicle. This number is included in axleCount , hence
    trailerAxleCount must be less than axleCount and greater than or
    equal to 1. axleCount and trailerCount are required to specify
    trailerAxleCount . By default, it is not set. Note: : This parameter
    is currently used only for the calculation of tolls in regions where
    it is applicable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-kingpinToRearAxleDistanceInCentimeters"
    class="section detail">

    ### kingpinToRearAxleDistanceInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">kingpinToRearAxleDistanceInCentimeters</span>

    </div>

    <div class="block">

    Defines the kingpin to rear axle distance, in centimeters. NOTE:
    Currently, the KPRA restrictions are only present in California and
    Idaho. Note: Supported in TransportMode.TRUCK , TransportMode.CAR
    (Beta), TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-emptyWeightInKilograms"
    class="section detail">

    ### emptyWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">emptyWeightInKilograms</span>

    </div>

    <div class="block">

    Empty weight of the vehicle without any load, excluding trailers,
    specified in kilograms. The provided value must be greater than or
    equal to 0. By default, it is not set. Note: Supported in
    TransportMode.TRUCK , TransportMode.BUS , TransportMode.PRIVATE_BUS
    , TransportMode.CAR (Beta), TransportMode.TAXI (Beta) transport
    modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-grossWeightInKilograms"
    class="section detail">

    ### grossWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">grossWeightInKilograms</span>

    </div>

    <div class="block">

    Gross truck weight, including trailers and shipped goods when loaded
    at capacity, specified in kilograms. The provided value must be
    greater than or equal to 0. If unspecified, it will default to
    currentWeightInKilograms . By default, it is not set. Notes:
    Supported in TransportMode.TRUCK , TransportMode.BUS ,
    TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes. Maximum weight for a car
    or taxi without a trailer is 4250 kg. Maximum weight for a car or
    taxi with a trailer is 7550 kg.

    </div>

    </div>

  - <div id="sdk-for-android-explore-currentWeightInKilograms"
    class="section detail">

    ### currentWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">currentWeightInKilograms</span>

    </div>

    <div class="block">

    Current truck weight, including trailers and shipped goods currently
    loaded, specified in kilograms. The provided value must be greater
    than or equal to 0. If unspecified, it will default to
    grossWeightInKilograms . By default, it is not set. Notes: Supported
    in TransportMode.TRUCK , TransportMode.BUS ,
    TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes. Maximum weight for a car
    or taxi without a trailer is 5000 kg. Maximum weight for a car or
    taxi with a trailer is 8500 kg. A route request with
    currentWeightInKilograms above grossWeightInKilograms may result in
    non-compliant or invalid routes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-weightPerAxleInKilograms"
    class="section detail">

    ### weightPerAxleInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">weightPerAxleInKilograms</span>

    </div>

    <div class="block">

    Heaviest weight per axle, regardless of axle type or axle group. It
    is evaluated against all axle weight restrictions, including single
    axle and tandem axle weight restrictions. The provided value must be
    greater or equal to 0. By default, it is not set. Notes:
    weightPerAxleInKilograms and weightPerAxleGroup are incompatible.
    When available for your edition, if both attributes are set, during
    online RoutingEngine an RoutingError.INVALID_PARAMETER error is
    generated. Otherwise, when offline RoutingEngine is in place, both
    parameters are evaluated and the maximum value between them will be
    used. Supported in TransportMode.TRUCK , TransportMode.BUS ,
    TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-weightPerAxleGroup"
    class="section detail">

    ### weightPerAxleGroup

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[WeightPerAxleGroup](sdk-for-android-explore-com-here-sdk-transport-weightperaxlegroup "class in com.here.sdk.transport")</span> <span class="element-name">weightPerAxleGroup</span>

    </div>

    <div class="block">

    Allows specification of axle weights in a more fine-grained way than
    weightPerAxleInKilograms . This is relevant in countries with signs
    and regulations that specify different limits for different axle
    groups, like the USA and Sweden. By default is not set. Notes:
    weightPerAxleInKilograms and weightPerAxleGroup are incompatible.
    When available for your edition, if both attributes are set, during
    online RoutingEngine an RoutingError.INVALID_PARAMETER error is
    generated. Otherwise, when offline RoutingEngine is in place, both
    parameters are evaluated and the maximum value between them will be
    used. Supported in TransportMode.TRUCK , TransportMode.BUS ,
    TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-isCommercial"
    class="section detail">

    ### isCommercial

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCommercial</span>

    </div>

    <div class="block">

    Specifies whether the vehicle is a commercial or a non-commercial
    vehicle. Defaults to false . Notes Only supported for online
    routing. This parameter is currently used only for the calculation
    of tolls in regions where it is applicable. Not used for offline
    calculations. Supported for TransportMode.CAR , TransportMode.TRUCK
    , TransportMode.BUS , TransportMode.PRIVATE_BUS and
    TransportMode.TAXI .

    </div>

    </div>

  - <div id="sdk-for-android-explore-lastCharacterOfLicensePlate"
    class="section detail">

    ### lastCharacterOfLicensePlate

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">lastCharacterOfLicensePlate</span>

    </div>

    <div class="block">

    Last character of license plate in String format. This value can be
    used to evaluate restrictions in environmental zones. By default, it
    is not set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-engineSizeInCubicCentimeters"
    class="section detail">

    ### engineSizeInCubicCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">engineSizeInCubicCentimeters</span>

    </div>

    <div class="block">

    Engine size of the scooter in cubic centimeters. Shouldn't be less
    than 1 or greater than 65535. Default value is null , which means
    the scooter route calculation ignores all engine size limits on the
    road. Notes For now, this option is only relevant in Japan and will
    be ignored for other countries. Currently, map data for this option
    is only available for Japan. Supported only in TransportMode.SCOOTER
    (Alpha) transport mode.

    </div>

    </div>

  - <div id="sdk-for-android-explore-tiresCount" class="section detail">

    ### tiresCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">tiresCount</span>

    </div>

    <div class="block">

    The total number of tires the vehicle has, i.e., the tires on the
    base vehicle and any attached trailers. By default, it is not set.
    Otherwise it is guaranteed to be in the range \[1, 255\]. Note :
    This parameter is not supported in isoline routing.

    </div>

    </div>

  - <div id="sdk-for-android-explore-tunnelCategory"
    class="section detail">

    ### tunnelCategory

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TunnelCategory](sdk-for-android-explore-com-here-sdk-transport-tunnelcategory "enum class in com.here.sdk.transport")</span> <span class="element-name">tunnelCategory</span>

    </div>

    <div class="block">

    Specifies the tunnel categories to restrict certain route links. The
    route will pass only through tunnels of a less strict category.
    Refer to TunnelCategory for the available options. By default, it is
    not set. Note: Supported in TransportMode.TRUCK , TransportMode.BUS
    , TransportMode.PRIVATE_BUS , TransportMode.CAR (Beta),
    TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-hazardousMaterials"
    class="section detail">

    ### hazardousMaterials

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[HazardousMaterial](sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial "enum class in com.here.sdk.transport")></span> <span class="element-name">hazardousMaterials</span>

    </div>

    <div class="block">

    Specifies a list of hazardous materials shipped in the vehicle.
    Refer to HazardousMaterial for the available options. By default, it
    is an empty list. Note: Supported in TransportMode.TRUCK ,
    TransportMode.BUS , TransportMode.PRIVATE_BUS , TransportMode.CAR
    (Beta), TransportMode.TAXI (Beta) transport modes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-occupancy" class="section detail">

    ### occupancy

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">occupancy</span>

    </div>

    <div class="block">

    Specifies the number of occupants in the vehicle, including driver,
    can affect the vehicle's ability to use HOV/carpool restricted
    lanes. Should not be less than 1 or greater than 255. By default, it
    is not set.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### VehicleSpecification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleSpecification</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

