---
title: "VehicleRestriction Structure Reference"
slug: "sdk-for-ios-explore-api-reference-classes-trafficincident-vehiclerestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VehicleRestriction.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestriction"></a>
<a title="VehicleRestriction Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Traffic.html">Traffic</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Classes/TrafficIncident.html">TrafficIncident</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        VehicleRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct VehicleRestriction : Hashable</code></pre>
</div>
</div>
<p>The vehicle restriction representing a vehicle category and relevant restriction rules.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV18isRestrictedAlwaysSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRestrictedAlways"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV18isRestrictedAlwaysSbvp">isRestrictedAlways</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if vehicles of the matching category are restricted anyway (not depending on any vehicle parameter).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isRestrictedAlways: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV22isDieselFuelRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDieselFuelRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV22isDieselFuelRestrictedSbvp">isDieselFuelRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if diesel fuel is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isDieselFuelRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV22isPetrolFuelRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPetrolFuelRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV22isPetrolFuelRestrictedSbvp">isPetrolFuelRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if petrol fuel is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isPetrolFuelRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isLpgFuelRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isLpgFuelRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isLpgFuelRestrictedSbvp">isLpgFuelRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if LPG fuel is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isLpgFuelRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isCaravanRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCaravanRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isCaravanRestrictedSbvp">isCaravanRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a driving with a caravan is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isCaravanRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isTrailerRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTrailerRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV19isTrailerRestrictedSbvp">isTrailerRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a driving with a trailer is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isTrailerRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV36isDrivingWithoutSnowChainsRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDrivingWithoutSnowChainsRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV36isDrivingWithoutSnowChainsRestrictedSbvp">isDrivingWithoutSnowChainsRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a driving without snow chains is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isDrivingWithoutSnowChainsRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV37isDrivingWithoutWinterTyresRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDrivingWithoutWinterTyresRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV37isDrivingWithoutWinterTyresRestrictedSbvp">isDrivingWithoutWinterTyresRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a driving without winter tyres is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isDrivingWithoutWinterTyresRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV27isEvenNumberPlateRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEvenNumberPlateRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV27isEvenNumberPlateRestrictedSbvp">isEvenNumberPlateRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a plate with even number is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isEvenNumberPlateRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV26isOddNumberPlateRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isOddNumberPlateRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV26isOddNumberPlateRestrictedSbvp">isOddNumberPlateRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a plate with odd number is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isOddNumberPlateRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV09isThroughB10RestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isThroughTrafficRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV09isThroughB10RestrictedSbvp">isThroughTrafficRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a through traffic is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isThroughTrafficRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV011isResidentsB10RestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isResidentsTrafficRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV011isResidentsB10RestrictedSbvp">isResidentsTrafficRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a residents traffic is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isResidentsTrafficRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV015isDestinationInC14AreaRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDestinationInIncidentAreaRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV015isDestinationInC14AreaRestrictedSbvp">isDestinationInIncidentAreaRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if a traffic destination in the incident area is restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isDestinationInIncidentAreaRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro3EmissionStandardRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEuro3EmissionStandardRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro3EmissionStandardRestrictedSbvp">isEuro3EmissionStandardRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if euro3 and weaker emission standards are restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isEuro3EmissionStandardRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro4EmissionStandardRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEuro4EmissionStandardRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro4EmissionStandardRestrictedSbvp">isEuro4EmissionStandardRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if euro4 and weaker emission standards are restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isEuro4EmissionStandardRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro5EmissionStandardRestrictedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isEuro5EmissionStandardRestricted"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV33isEuro5EmissionStandardRestrictedSbvp">isEuro5EmissionStandardRestricted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The flag indicating if euro5 and weaker emission standards are restricted for vehicles of the matching category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var isEuro5EmissionStandardRestricted: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV42restrictedIfGrossWeightMoreThanInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfGrossWeightMoreThanInKilograms"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV42restrictedIfGrossWeightMoreThanInKilogramss5Int32VSgvp">restrictedIfGrossWeightMoreThanInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle gross weight is more than the weight in kilograms.
If the value is <code>nil</code> the upper gross weight bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfGrossWeightMoreThanInKilograms: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV42restrictedIfGrossWeightLessThanInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfGrossWeightLessThanInKilograms"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV42restrictedIfGrossWeightLessThanInKilogramss5Int32VSgvp">restrictedIfGrossWeightLessThanInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle gross weight is less than the weight in kilograms.
If the value is <code>nil</code> the lower gross weight bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfGrossWeightLessThanInKilograms: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV41restrictedIfAxleWeightMoreThanInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfAxleWeightMoreThanInKilograms"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV41restrictedIfAxleWeightMoreThanInKilogramss5Int32VSgvp">restrictedIfAxleWeightMoreThanInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle weight per axle is more than the weight in kilograms.
If the value is <code>nil</code> the upper weight per axle bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfAxleWeightMoreThanInKilograms: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV41restrictedIfAxleWeightLessThanInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfAxleWeightLessThanInKilograms"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV41restrictedIfAxleWeightLessThanInKilogramss5Int32VSgvp">restrictedIfAxleWeightLessThanInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle weight per axle is less than the weight in kilograms.
If the value is <code>nil</code> the lower weight per axle bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfAxleWeightLessThanInKilograms: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV35restrictedIfLongerThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfLongerThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV35restrictedIfLongerThanInCentimeterss5Int32VSgvp">restrictedIfLongerThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is longer than the length in centimeters.
If the value is <code>nil</code> the upper length bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfLongerThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV36restrictedIfShorterThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfShorterThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV36restrictedIfShorterThanInCentimeterss5Int32VSgvp">restrictedIfShorterThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is shorter than the length in centimeters.
If the value is <code>nil</code> the lower length bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfShorterThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV35restrictedIfHigherThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfHigherThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV35restrictedIfHigherThanInCentimeterss5Int32VSgvp">restrictedIfHigherThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is higher than the height in centimeters.
If the value is <code>nil</code> the upper height bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfHigherThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV34restrictedIfLowerThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfLowerThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV34restrictedIfLowerThanInCentimeterss5Int32VSgvp">restrictedIfLowerThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is lower than the height in centimeters.
If the value is <code>nil</code> the lower height bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfLowerThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV34restrictedIfWiderThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfWiderThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV34restrictedIfWiderThanInCentimeterss5Int32VSgvp">restrictedIfWiderThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is wider than the width in centimeters.
If the value is <code>nil</code> the upper width bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfWiderThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV37restrictedIfNarrowerThanInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfNarrowerThanInCentimeters"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV37restrictedIfNarrowerThanInCentimeterss5Int32VSgvp">restrictedIfNarrowerThanInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the vehicle is narrower than the width in centimeters.
If the value is <code>nil</code> the lower width bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfNarrowerThanInCentimeters: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV29restrictedIfOccupantsMoreThans5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfOccupantsMoreThan"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV29restrictedIfOccupantsMoreThans5Int32VSgvp">restrictedIfOccupantsMoreThan</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the occupants number is more than the value.
If the value is <code>nil</code> the upper occupants bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfOccupantsMoreThan: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV30restrictedIfOccupantsFewerThans5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/restrictedIfOccupantsFewerThan"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV30restrictedIfOccupantsFewerThans5Int32VSgvp">restrictedIfOccupantsFewerThan</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicles of the matching category are restricted if the occupants number is fewer than the value.
If the value is <code>nil</code> the lower occupants bound is not specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var restrictedIfOccupantsFewerThan: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficIncidentC18VehicleRestrictionV18isRestrictedAlways0f10DieselFuelG00f6PetroljG00f3LpgjG00f7CaravanG00f7TrailerG00f24DrivingWithoutSnowChainsG00fop11WinterTyresG00f15EvenNumberPlateG00f3OddvwG00f7ThroughbG00f9ResidentsbG00f13DestinationInc4AreaG00f21Euro3EmissionStandardG00f21Euro4EmissionStandardG00f21Euro5EmissionStandardG042restrictedIfGrossWeightMoreThanInKilograms42restrictedIfGrossWeightLessThanInKilograms41restrictedIfAxleWeightMoreThanInKilograms41restrictedIfAxleWeightLessThanInKilograms35restrictedIfLongerThanInCentimeters36restrictedIfShorterThanInCentimeters35restrictedIfHigherThanInCentimeters34restrictedIfLowerThanInCentimeters34restrictedIfWiderThanInCentimeters37restrictedIfNarrowerThanInCentimeters29restrictedIfOccupantsMoreThan30restrictedIfOccupantsFewerThanAESb_S15bs5Int32VSgA8_A8_A8_A8_A8_A8_A8_A8_A8_A8_A8_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isRestrictedAlways:isDieselFuelRestricted:isPetrolFuelRestricted:isLpgFuelRestricted:isCaravanRestricted:isTrailerRestricted:isDrivingWithoutSnowChainsRestricted:isDrivingWithoutWinterTyresRestricted:isEvenNumberPlateRestricted:isOddNumberPlateRestricted:isThroughTrafficRestricted:isResidentsTrafficRestricted:isDestinationInIncidentAreaRestricted:isEuro3EmissionStandardRestricted:isEuro4EmissionStandardRestricted:isEuro5EmissionStandardRestricted:restrictedIfGrossWeightMoreThanInKilograms:restrictedIfGrossWeightLessThanInKilograms:restrictedIfAxleWeightMoreThanInKilograms:restrictedIfAxleWeightLessThanInKilograms:restrictedIfLongerThanInCentimeters:restrictedIfShorterThanInCentimeters:restrictedIfHigherThanInCentimeters:restrictedIfLowerThanInCentimeters:restrictedIfWiderThanInCentimeters:restrictedIfNarrowerThanInCentimeters:restrictedIfOccupantsMoreThan:restrictedIfOccupantsFewerThan:)"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC18VehicleRestrictionV18isRestrictedAlways0f10DieselFuelG00f6PetroljG00f3LpgjG00f7CaravanG00f7TrailerG00f24DrivingWithoutSnowChainsG00fop11WinterTyresG00f15EvenNumberPlateG00f3OddvwG00f7ThroughbG00f9ResidentsbG00f13DestinationInc4AreaG00f21Euro3EmissionStandardG00f21Euro4EmissionStandardG00f21Euro5EmissionStandardG042restrictedIfGrossWeightMoreThanInKilograms42restrictedIfGrossWeightLessThanInKilograms41restrictedIfAxleWeightMoreThanInKilograms41restrictedIfAxleWeightLessThanInKilograms35restrictedIfLongerThanInCentimeters36restrictedIfShorterThanInCentimeters35restrictedIfHigherThanInCentimeters34restrictedIfLowerThanInCentimeters34restrictedIfWiderThanInCentimeters37restrictedIfNarrowerThanInCentimeters29restrictedIfOccupantsMoreThan30restrictedIfOccupantsFewerThanAESb_S15bs5Int32VSgA8_A8_A8_A8_A8_A8_A8_A8_A8_A8_A8_tcfc">init(isRestrictedAlways:<wbr/>isDieselFuelRestricted:<wbr/>isPetrolFuelRestricted:<wbr/>isLpgFuelRestricted:<wbr/>isCaravanRestricted:<wbr/>isTrailerRestricted:<wbr/>isDrivingWithoutSnowChainsRestricted:<wbr/>isDrivingWithoutWinterTyresRestricted:<wbr/>isEvenNumberPlateRestricted:<wbr/>isOddNumberPlateRestricted:<wbr/>isThroughTrafficRestricted:<wbr/>isResidentsTrafficRestricted:<wbr/>isDestinationInIncidentAreaRestricted:<wbr/>isEuro3EmissionStandardRestricted:<wbr/>isEuro4EmissionStandardRestricted:<wbr/>isEuro5EmissionStandardRestricted:<wbr/>restrictedIfGrossWeightMoreThanInKilograms:<wbr/>restrictedIfGrossWeightLessThanInKilograms:<wbr/>restrictedIfAxleWeightMoreThanInKilograms:<wbr/>restrictedIfAxleWeightLessThanInKilograms:<wbr/>restrictedIfLongerThanInCentimeters:<wbr/>restrictedIfShorterThanInCentimeters:<wbr/>restrictedIfHigherThanInCentimeters:<wbr/>restrictedIfLowerThanInCentimeters:<wbr/>restrictedIfWiderThanInCentimeters:<wbr/>restrictedIfNarrowerThanInCentimeters:<wbr/>restrictedIfOccupantsMoreThan:<wbr/>restrictedIfOccupantsFewerThan:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(isRestrictedAlways: Bool = false, isDieselFuelRestricted: Bool = false, isPetrolFuelRestricted: Bool = false, isLpgFuelRestricted: Bool = false, isCaravanRestricted: Bool = false, isTrailerRestricted: Bool = false, isDrivingWithoutSnowChainsRestricted: Bool = false, isDrivingWithoutWinterTyresRestricted: Bool = false, isEvenNumberPlateRestricted: Bool = false, isOddNumberPlateRestricted: Bool = false, isThroughTrafficRestricted: Bool = false, isResidentsTrafficRestricted: Bool = false, isDestinationInIncidentAreaRestricted: Bool = false, isEuro3EmissionStandardRestricted: Bool = false, isEuro4EmissionStandardRestricted: Bool = false, isEuro5EmissionStandardRestricted: Bool = false, restrictedIfGrossWeightMoreThanInKilograms: Int32? = nil, restrictedIfGrossWeightLessThanInKilograms: Int32? = nil, restrictedIfAxleWeightMoreThanInKilograms: Int32? = nil, restrictedIfAxleWeightLessThanInKilograms: Int32? = nil, restrictedIfLongerThanInCentimeters: Int32? = nil, restrictedIfShorterThanInCentimeters: Int32? = nil, restrictedIfHigherThanInCentimeters: Int32? = nil, restrictedIfLowerThanInCentimeters: Int32? = nil, restrictedIfWiderThanInCentimeters: Int32? = nil, restrictedIfNarrowerThanInCentimeters: Int32? = nil, restrictedIfOccupantsMoreThan: Int32? = nil, restrictedIfOccupantsFewerThan: Int32? = nil)</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
