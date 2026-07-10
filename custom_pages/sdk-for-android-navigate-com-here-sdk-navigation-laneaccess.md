---
title: "LaneAccess (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-laneaccess"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.LaneAccess → com.here.sdk.navigation.LaneAccess

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LaneAccess</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class which identifies the vehicle type(s) allowed to access a lane.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#automobiles" class="member-name-link"><code>automobiles</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#buses" class="member-name-link"><code>buses</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Buses that are used for public transportation.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#carpools" class="member-name-link"><code>carpools</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#deliveryVehicles" class="member-name-link"><code>deliveryVehicles</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Delivery trucks that are permitted to enter the city proper to unload goods at businesses.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#emergencyVehicles" class="member-name-link"><code>emergencyVehicles</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#motorcycles" class="member-name-link"><code>motorcycles</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Motorized two-wheeled passenger vehicles.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#pedestrians" class="member-name-link"><code>pedestrians</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Persons traveling on foot, whether walking or running.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#taxis" class="member-name-link"><code>taxis</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#throughTraffic" class="member-name-link"><code>throughTraffic</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks" class="member-name-link"><code>trucks</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Large vehicles that range from medium to heavy duty trucks.

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

      LaneAccess (boolean automobiles,
       boolean buses,
       boolean taxis,
       boolean carpools,
       boolean pedestrians,
       boolean trucks,
       boolean throughTraffic,
       boolean deliveryVehicles,
       boolean emergencyVehicles,
       boolean motorcycles)

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

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-automobiles" class="section detail">

    ### automobiles

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">automobiles</span>

    </div>

    <div class="block">

    Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-buses" class="section detail">

    ### buses

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">buses</span>

    </div>

    <div class="block">

    Buses that are used for public transportation.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-taxis" class="section detail">

    ### taxis

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">taxis</span>

    </div>

    <div class="block">

    Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-carpools" class="section detail">

    ### carpools

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">carpools</span>

    </div>

    <div class="block">

    Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-pedestrians" class="section detail">

    ### pedestrians

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">pedestrians</span>

    </div>

    <div class="block">

    Persons traveling on foot, whether walking or running.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-trucks" class="section detail">

    ### trucks

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">trucks</span>

    </div>

    <div class="block">

    Large vehicles that range from medium to heavy duty trucks.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-throughTraffic" class="section detail">

    ### throughTraffic

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">throughTraffic</span>

    </div>

    <div class="block">

    Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-deliveryVehicles" class="section detail">

    ### deliveryVehicles

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">deliveryVehicles</span>

    </div>

    <div class="block">

    Delivery trucks that are permitted to enter the city proper to unload goods at businesses.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-emergencyVehicles" class="section detail">

    ### emergencyVehicles

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">emergencyVehicles</span>

    </div>

    <div class="block">

    Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-motorcycles" class="section detail">

    ### motorcycles

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">motorcycles</span>

    </div>

    <div class="block">

    Motorized two-wheeled passenger vehicles. Generally, mopeds are considered motorcycles.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean" class="section detail">

    ### LaneAccess

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LaneAccess</span><wbr></wbr><span class="parameters">(boolean automobiles, boolean buses, boolean taxis, boolean carpools, boolean pedestrians, boolean trucks, boolean throughTraffic, boolean deliveryVehicles, boolean emergencyVehicles, boolean motorcycles)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `automobiles` -

    Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.

    `buses` -

    Buses that are used for public transportation.

    `taxis` -

    Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.

    `carpools` -

    Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.

    `pedestrians` -

    Persons traveling on foot, whether walking or running.

    `trucks` -

    Large vehicles that range from medium to heavy duty trucks.

    `throughTraffic` -

    Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.

    `deliveryVehicles` -

    Delivery <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks">`trucks`</a> that are permitted to enter the city proper to unload goods at businesses.

    `emergencyVehicles` -

    Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.

    `motorcycles` -

    Motorized two-wheeled passenger vehicles. Generally, mopeds are considered motorcycles.

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

