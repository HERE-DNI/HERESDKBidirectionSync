---
title: "TrafficIncident.VehicleRestriction (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.traffic.TrafficIncident.VehicleRestriction

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[TrafficIncident](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">TrafficIncident.VehicleRestriction</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The vehicle restriction representing a vehicle category and relevant
restriction rules.

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
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isCaravanRestricted"
  class="member-name-link"><code>isCaravanRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a driving with a caravan is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isDestinationInIncidentAreaRestricted"
  class="member-name-link"><code>isDestinationInIncidentAreaRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a traffic destination in the incident area is
  restricted for vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isDieselFuelRestricted"
  class="member-name-link"><code>isDieselFuelRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if diesel fuel is restricted for vehicles of the
  matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isDrivingWithoutSnowChainsRestricted"
  class="member-name-link"><code>isDrivingWithoutSnowChainsRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a driving without snow chains is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isDrivingWithoutWinterTyresRestricted"
  class="member-name-link"><code>isDrivingWithoutWinterTyresRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a driving without winter tyres is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isEuro3EmissionStandardRestricted"
  class="member-name-link"><code>isEuro3EmissionStandardRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if euro3 and weaker emission standards are
  restricted for vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isEuro4EmissionStandardRestricted"
  class="member-name-link"><code>isEuro4EmissionStandardRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if euro4 and weaker emission standards are
  restricted for vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isEuro5EmissionStandardRestricted"
  class="member-name-link"><code>isEuro5EmissionStandardRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if euro5 and weaker emission standards are
  restricted for vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isEvenNumberPlateRestricted"
  class="member-name-link"><code>isEvenNumberPlateRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a plate with even number is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isLpgFuelRestricted"
  class="member-name-link"><code>isLpgFuelRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if LPG fuel is restricted for vehicles of the
  matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isOddNumberPlateRestricted"
  class="member-name-link"><code>isOddNumberPlateRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a plate with odd number is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isPetrolFuelRestricted"
  class="member-name-link"><code>isPetrolFuelRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if petrol fuel is restricted for vehicles of the
  matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isResidentsTrafficRestricted"
  class="member-name-link"><code>isResidentsTrafficRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a residents traffic is restricted for vehicles of
  the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isRestrictedAlways"
  class="member-name-link"><code>isRestrictedAlways</code></a></td>
  <td><div class="block">
  The flag indicating if vehicles of the matching category are restricted
  anyway (not depending on any vehicle parameter).
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isThroughTrafficRestricted"
  class="member-name-link"><code>isThroughTrafficRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a through traffic is restricted for vehicles of
  the matching category.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#isTrailerRestricted"
  class="member-name-link"><code>isTrailerRestricted</code></a></td>
  <td><div class="block">
  The flag indicating if a driving with a trailer is restricted for
  vehicles of the matching category.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfAxleWeightLessThanInKilograms"
  class="member-name-link"><code>restrictedIfAxleWeightLessThanInKilograms</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle weight
  per axle is less than the weight in kilograms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfAxleWeightMoreThanInKilograms"
  class="member-name-link"><code>restrictedIfAxleWeightMoreThanInKilograms</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle weight
  per axle is more than the weight in kilograms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfGrossWeightLessThanInKilograms"
  class="member-name-link"><code>restrictedIfGrossWeightLessThanInKilograms</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle gross
  weight is less than the weight in kilograms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfGrossWeightMoreThanInKilograms"
  class="member-name-link"><code>restrictedIfGrossWeightMoreThanInKilograms</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle gross
  weight is more than the weight in kilograms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfHigherThanInCentimeters"
  class="member-name-link"><code>restrictedIfHigherThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is
  higher than the height in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfLongerThanInCentimeters"
  class="member-name-link"><code>restrictedIfLongerThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is
  longer than the length in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfLowerThanInCentimeters"
  class="member-name-link"><code>restrictedIfLowerThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is lower
  than the height in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfNarrowerThanInCentimeters"
  class="member-name-link"><code>restrictedIfNarrowerThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is
  narrower than the width in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfOccupantsFewerThan"
  class="member-name-link"><code>restrictedIfOccupantsFewerThan</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the occupants number
  is fewer than the value.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfOccupantsMoreThan"
  class="member-name-link"><code>restrictedIfOccupantsMoreThan</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the occupants number
  is more than the value.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfShorterThanInCentimeters"
  class="member-name-link"><code>restrictedIfShorterThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is
  shorter than the length in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction#restrictedIfWiderThanInCentimeters"
  class="member-name-link"><code>restrictedIfWiderThanInCentimeters</code></a></td>
  <td><div class="block">
  Vehicles of the matching category are restricted if the vehicle is wider
  than the width in centimeters.
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
  <td><pre><code>VehicleRestriction()</code></pre></td>
  <td><div class="block">
  Creates a new instance with default values.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

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

- <div id="field-detail" class="section field-details">

  - <div id="isRestrictedAlways" class="section detail">

    ### isRestrictedAlways

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRestrictedAlways</span>

    </div>

    <div class="block">

    The flag indicating if vehicles of the matching category are
    restricted anyway (not depending on any vehicle parameter).

    </div>

    </div>

  - <div id="isDieselFuelRestricted" class="section detail">

    ### isDieselFuelRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDieselFuelRestricted</span>

    </div>

    <div class="block">

    The flag indicating if diesel fuel is restricted for vehicles of the
    matching category.

    </div>

    </div>

  - <div id="isPetrolFuelRestricted" class="section detail">

    ### isPetrolFuelRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPetrolFuelRestricted</span>

    </div>

    <div class="block">

    The flag indicating if petrol fuel is restricted for vehicles of the
    matching category.

    </div>

    </div>

  - <div id="isLpgFuelRestricted" class="section detail">

    ### isLpgFuelRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLpgFuelRestricted</span>

    </div>

    <div class="block">

    The flag indicating if LPG fuel is restricted for vehicles of the
    matching category.

    </div>

    </div>

  - <div id="isCaravanRestricted" class="section detail">

    ### isCaravanRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCaravanRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a driving with a caravan is restricted for
    vehicles of the matching category.

    </div>

    </div>

  - <div id="isTrailerRestricted" class="section detail">

    ### isTrailerRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTrailerRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a driving with a trailer is restricted for
    vehicles of the matching category.

    </div>

    </div>

  - <div id="isDrivingWithoutSnowChainsRestricted"
    class="section detail">

    ### isDrivingWithoutSnowChainsRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingWithoutSnowChainsRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a driving without snow chains is restricted
    for vehicles of the matching category.

    </div>

    </div>

  - <div id="isDrivingWithoutWinterTyresRestricted"
    class="section detail">

    ### isDrivingWithoutWinterTyresRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingWithoutWinterTyresRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a driving without winter tyres is restricted
    for vehicles of the matching category.

    </div>

    </div>

  - <div id="isEvenNumberPlateRestricted" class="section detail">

    ### isEvenNumberPlateRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEvenNumberPlateRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a plate with even number is restricted for
    vehicles of the matching category.

    </div>

    </div>

  - <div id="isOddNumberPlateRestricted" class="section detail">

    ### isOddNumberPlateRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOddNumberPlateRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a plate with odd number is restricted for
    vehicles of the matching category.

    </div>

    </div>

  - <div id="isThroughTrafficRestricted" class="section detail">

    ### isThroughTrafficRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isThroughTrafficRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a through traffic is restricted for vehicles
    of the matching category.

    </div>

    </div>

  - <div id="isResidentsTrafficRestricted" class="section detail">

    ### isResidentsTrafficRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isResidentsTrafficRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a residents traffic is restricted for
    vehicles of the matching category.

    </div>

    </div>

  - <div id="isDestinationInIncidentAreaRestricted"
    class="section detail">

    ### isDestinationInIncidentAreaRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDestinationInIncidentAreaRestricted</span>

    </div>

    <div class="block">

    The flag indicating if a traffic destination in the incident area is
    restricted for vehicles of the matching category.

    </div>

    </div>

  - <div id="isEuro3EmissionStandardRestricted" class="section detail">

    ### isEuro3EmissionStandardRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro3EmissionStandardRestricted</span>

    </div>

    <div class="block">

    The flag indicating if euro3 and weaker emission standards are
    restricted for vehicles of the matching category.

    </div>

    </div>

  - <div id="isEuro4EmissionStandardRestricted" class="section detail">

    ### isEuro4EmissionStandardRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro4EmissionStandardRestricted</span>

    </div>

    <div class="block">

    The flag indicating if euro4 and weaker emission standards are
    restricted for vehicles of the matching category.

    </div>

    </div>

  - <div id="isEuro5EmissionStandardRestricted" class="section detail">

    ### isEuro5EmissionStandardRestricted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro5EmissionStandardRestricted</span>

    </div>

    <div class="block">

    The flag indicating if euro5 and weaker emission standards are
    restricted for vehicles of the matching category.

    </div>

    </div>

  - <div id="restrictedIfGrossWeightMoreThanInKilograms"
    class="section detail">

    ### restrictedIfGrossWeightMoreThanInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfGrossWeightMoreThanInKilograms</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle
    gross weight is more than the weight in kilograms. If the value is
    null the upper gross weight bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfGrossWeightLessThanInKilograms"
    class="section detail">

    ### restrictedIfGrossWeightLessThanInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfGrossWeightLessThanInKilograms</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle
    gross weight is less than the weight in kilograms. If the value is
    null the lower gross weight bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfAxleWeightMoreThanInKilograms"
    class="section detail">

    ### restrictedIfAxleWeightMoreThanInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfAxleWeightMoreThanInKilograms</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle
    weight per axle is more than the weight in kilograms. If the value
    is null the upper weight per axle bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfAxleWeightLessThanInKilograms"
    class="section detail">

    ### restrictedIfAxleWeightLessThanInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfAxleWeightLessThanInKilograms</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle
    weight per axle is less than the weight in kilograms. If the value
    is null the lower weight per axle bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfLongerThanInCentimeters"
    class="section detail">

    ### restrictedIfLongerThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfLongerThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    longer than the length in centimeters. If the value is null the
    upper length bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfShorterThanInCentimeters"
    class="section detail">

    ### restrictedIfShorterThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfShorterThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    shorter than the length in centimeters. If the value is null the
    lower length bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfHigherThanInCentimeters"
    class="section detail">

    ### restrictedIfHigherThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfHigherThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    higher than the height in centimeters. If the value is null the
    upper height bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfLowerThanInCentimeters" class="section detail">

    ### restrictedIfLowerThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfLowerThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    lower than the height in centimeters. If the value is null the lower
    height bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfWiderThanInCentimeters" class="section detail">

    ### restrictedIfWiderThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfWiderThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    wider than the width in centimeters. If the value is null the upper
    width bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfNarrowerThanInCentimeters"
    class="section detail">

    ### restrictedIfNarrowerThanInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfNarrowerThanInCentimeters</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the vehicle is
    narrower than the width in centimeters. If the value is null the
    lower width bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfOccupantsMoreThan" class="section detail">

    ### restrictedIfOccupantsMoreThan

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfOccupantsMoreThan</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the occupants
    number is more than the value. If the value is null the upper
    occupants bound is not specified.

    </div>

    </div>

  - <div id="restrictedIfOccupantsFewerThan" class="section detail">

    ### restrictedIfOccupantsFewerThan

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfOccupantsFewerThan</span>

    </div>

    <div class="block">

    Vehicles of the matching category are restricted if the occupants
    number is fewer than the value. If the value is null the lower
    occupants bound is not specified.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### VehicleRestriction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span>()

    </div>

    <div class="block">

    Creates a new instance with default values.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

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

  - <div id="hashCode()" class="section detail">

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

