---
title: "TrafficIncident.RestrictedVehicleCategory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \<
TrafficIncident.RestrictedVehicleCategory \>
com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory →
java.lang.Enum \< TrafficIncident.RestrictedVehicleCategory \>
com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory →
com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<!-- -->

Enclosing class:  
[TrafficIncident](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic")

<div class="type-signature">

<span class="modifiers">public static enum
</span><span class="element-name type-name-label">TrafficIncident.RestrictedVehicleCategory</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a>\<[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")\></span>

</div>

<div class="block">

The vehicle categories that can be restricted. Note, a vehicle can
belong to several categories (e.g. a passenger motor car belongs to CAR
, MOTOR_VEHICLE , and ALL ). A vehicle is restricted if it belongs to
the category presented in the map
TrafficIncident.getVehicleRestrictions() and at least one of the vehicle
properties is under the matching TrafficIncident.VehicleRestriction .

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary"
  class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#ALL"
  class="member-name-link"><code>ALL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All the vehicles are applicable for this category.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#BUS"
  class="member-name-link"><code>BUS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Bus.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#CAR"
  class="member-name-link"><code>CAR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Car.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#HEAVY_GOODS_VEHICLE"
  class="member-name-link"><code>HEAVY_GOODS_VEHICLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Heavy goods vehicle (or large goods vehicle).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#MOTOR_VEHICLE"
  class="member-name-link"><code>MOTOR_VEHICLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Motor vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#MOTORCYCLE"
  class="member-name-link"><code>MOTORCYCLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Motorcycle.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#OTHER"
  class="member-name-link"><code>OTHER</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Other vehicles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TAXI"
  class="member-name-link"><code>TAXI</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Taxi.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRAIN"
  class="member-name-link"><code>TRAIN</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Train.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRANSPORTING_ABNORMAL_SIZE_LOAD"
  class="member-name-link"><code>TRANSPORTING_ABNORMAL_SIZE_LOAD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Transporting an abnormal size load.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRANSPORTING_HAZARDOUS_GOODS"
  class="member-name-link"><code>TRANSPORTING_HAZARDOUS_GOODS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Transporting hazardous goods.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRUCK"
  class="member-name-link"><code>TRUCK</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Truck.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#VEHICLE_WITH_TRAILER"
  class="member-name-link"><code>VEHICLE_WITH_TRAILER</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Vehicle with trailer.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the
  order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail"
  class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-BUS" class="section detail">

    ### BUS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">BUS</span>

    </div>

    <div class="block">

    Bus.

    </div>

    </div>

  - <div id="sdk-for-android-explore-CAR" class="section detail">

    ### CAR

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">CAR</span>

    </div>

    <div class="block">

    Car.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HEAVY_GOODS_VEHICLE"
    class="section detail">

    ### HEAVY_GOODS_VEHICLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">HEAVY_GOODS_VEHICLE</span>

    </div>

    <div class="block">

    Heavy goods vehicle (or large goods vehicle). In the European Union
    heavy goods vehicle is any truck with a gross combination mass (GCM)
    of over 3,500 kg.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRUCK" class="section detail">

    ### TRUCK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">TRUCK</span>

    </div>

    <div class="block">

    Truck.

    </div>

    </div>

  - <div id="sdk-for-android-explore-MOTORCYCLE" class="section detail">

    ### MOTORCYCLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">MOTORCYCLE</span>

    </div>

    <div class="block">

    Motorcycle.

    </div>

    </div>

  - <div id="sdk-for-android-explore-MOTOR_VEHICLE"
    class="section detail">

    ### MOTOR_VEHICLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">MOTOR_VEHICLE</span>

    </div>

    <div class="block">

    Motor vehicle. Definition: it is a self-propelled vehicle, that does
    not operate on rails and is used for the transportation of people or
    cargo.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TAXI" class="section detail">

    ### TAXI

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">TAXI</span>

    </div>

    <div class="block">

    Taxi.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRAIN" class="section detail">

    ### TRAIN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">TRAIN</span>

    </div>

    <div class="block">

    Train.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRANSPORTING_ABNORMAL_SIZE_LOAD"
    class="section detail">

    ### TRANSPORTING_ABNORMAL_SIZE_LOAD

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">TRANSPORTING_ABNORMAL_SIZE_LOAD</span>

    </div>

    <div class="block">

    Transporting an abnormal size load. See rules of the exact country
    that describe the exact parameters.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRANSPORTING_HAZARDOUS_GOODS"
    class="section detail">

    ### TRANSPORTING_HAZARDOUS_GOODS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">TRANSPORTING_HAZARDOUS_GOODS</span>

    </div>

    <div class="block">

    Transporting hazardous goods.

    </div>

    </div>

  - <div id="sdk-for-android-explore-VEHICLE_WITH_TRAILER"
    class="section detail">

    ### VEHICLE_WITH_TRAILER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">VEHICLE_WITH_TRAILER</span>

    </div>

    <div class="block">

    Vehicle with trailer.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OTHER" class="section detail">

    ### OTHER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">OTHER</span>

    </div>

    <div class="block">

    Other vehicles.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ALL" class="section detail">

    ### ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">ALL</span>

    </div>

    <div class="block">

    All the vehicles are applicable for this category.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String"
    class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

