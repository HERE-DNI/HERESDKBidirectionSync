---
title: "PhysicalConsumptionModel (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.PhysicalConsumptionModel →
com.here.sdk.routing.PhysicalConsumptionModel

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PhysicalConsumptionModel</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Defines the physical consumption model for electric vehicles, using
vehicle-specific parameters to calculate energy consumption along a
route. Note:
\[sdk.transport.VehicleSpecification.current_weight_in_kilograms\] must
be set. Note: This is a beta release of this feature, so there could be
a few bugs and unexpected behaviors. Related APIs may change for new
releases without a deprecation process.

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

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#airDragCoefficient"
  class="member-name-link"><code>airDragCoefficient</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The drag coefficient of an vehicle defines the way the vehicle is
  expected to pass through the surrounding air.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#auxiliaryPowerConsumptionInWatts"
  class="member-name-link"><code>auxiliaryPowerConsumptionInWatts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Power (in W) consumed by the vehicle's auxiliary systems (for example,
  air conditioning, lights).

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#driveTrainEfficiency"
  class="member-name-link"><code>driveTrainEfficiency</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The proportion of the energy drawn from the battery that is used to
  move the vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#frontalAreaInSquareMeters"
  class="member-name-link"><code>frontalAreaInSquareMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Frontal area represents the total cross section area of the vehicle as
  viewed from the front, specified in square meters.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#recuperationEfficiency"
  class="member-name-link"><code>recuperationEfficiency</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The proportion of the energy gained when braking or going downhill
  that can be recuperated and restored as battery charge.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel#rollingResistanceCoefficient"
  class="member-name-link"><code>rollingResistanceCoefficient</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Rolling resistance refers to the resistance experienced by your
  vehicle tire as it rolls over a surface.

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

      PhysicalConsumptionModel ()

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

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-driveTrainEfficiency"
    class="section detail">

    ### driveTrainEfficiency

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">driveTrainEfficiency</span>

    </div>

    <div class="block">

    The proportion of the energy drawn from the battery that is used to
    move the vehicle. (This is to factor in energy losses through heat
    in the motors, for example.) Supported range from 0 to 1

    </div>

    </div>

  - <div id="sdk-for-android-explore-recuperationEfficiency"
    class="section detail">

    ### recuperationEfficiency

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">recuperationEfficiency</span>

    </div>

    <div class="block">

    The proportion of the energy gained when braking or going downhill
    that can be recuperated and restored as battery charge. Supported
    range from 0 to 1

    </div>

    </div>

  - <div id="sdk-for-android-explore-auxiliaryPowerConsumptionInWatts"
    class="section detail">

    ### auxiliaryPowerConsumptionInWatts

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">auxiliaryPowerConsumptionInWatts</span>

    </div>

    <div class="block">

    Power (in W) consumed by the vehicle's auxiliary systems (for
    example, air conditioning, lights). The provided value must be
    greater than or equal to 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-frontalAreaInSquareMeters"
    class="section detail">

    ### frontalAreaInSquareMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">frontalAreaInSquareMeters</span>

    </div>

    <div class="block">

    Frontal area represents the total cross section area of the vehicle
    as viewed from the front, specified in square meters. Physical
    consumption model is using this value in combination with
    airDragCoefficient to calculate the consumption caused by air
    resistance. As fallback VehicleSpecification.widthInCentimeters and
    VehicleSpecification.heightInCentimeters are used. This parameter is
    used to provide a more accurate consumption prediction for electric
    vehicles. In the range from 0.5 to 50

    </div>

    </div>

  - <div id="sdk-for-android-explore-rollingResistanceCoefficient"
    class="section detail">

    ### rollingResistanceCoefficient

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">rollingResistanceCoefficient</span>

    </div>

    <div class="block">

    Rolling resistance refers to the resistance experienced by your
    vehicle tire as it rolls over a surface. The main causes of this
    resistance are tire deformation, wing drag, and friction with the
    ground. The coefficient of rolling resistance is a numerical value
    indicating the severity of this factor. This parameter is used to
    provide a more accurate consumption prediction for electric
    vehicles. Supported range from 0 to 1

    </div>

    </div>

  - <div id="sdk-for-android-explore-airDragCoefficient"
    class="section detail">

    ### airDragCoefficient

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">airDragCoefficient</span>

    </div>

    <div class="block">

    The drag coefficient of an vehicle defines the way the vehicle is
    expected to pass through the surrounding air. More streamlined
    vehicles are more aerodynamic and therefore have smaller drag
    coefficient. This parameter is used to provide a more accurate
    consumption prediction for electric vehicles. Supported range from 0
    to 1

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### PhysicalConsumptionModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PhysicalConsumptionModel</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object"
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

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

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

