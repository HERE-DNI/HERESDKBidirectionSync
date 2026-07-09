---
title: "LaneType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lanetype"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.LaneType → com.here.sdk.navigation.LaneType

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LaneType</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that provides information on the available lane properties. The lane type values can be combined as follows: High Occupancy Vehicle, Reversible High Occupancy Vehicle and Express Reversible and Express High Occupancy Vehicle, Reversible and Express High Occupancy Vehicle and Acceleration Reversible, Acceleration Lane High Occupancy Vehicle, Reversible, Acceleration Lane Express and Acceleration High Occupancy Vehicle and Deceleration Reversible, Deceleration Lane High Occupancy Vehicle, Reversible, Deceleration Lane Express and Deceleration

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isAcceleration" class="member-name-link"><code>isAcceleration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isAuxiliary" class="member-name-link"><code>isAuxiliary</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isBicycle" class="member-name-link"><code>isBicycle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isCenterTurn" class="member-name-link"><code>isCenterTurn</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isDeceleration" class="member-name-link"><code>isDeceleration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A deceleration lane is the same as an acceleration lane but used for the opposite scenario.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isExpress" class="member-name-link"><code>isExpress</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isHighOccupancyVehicle" class="member-name-link"><code>isHighOccupancyVehicle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A lane which is restricted for high occupancy vehicles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isParking" class="member-name-link"><code>isParking</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Parking lanes are portions of the road bed that may be used for parking legally.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isPassing" class="member-name-link"><code>isPassing</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads).

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isRegular" class="member-name-link"><code>isRegular</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Regular lane is a lane that does not have a specific use.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isRegulatedAccess" class="member-name-link"><code>isRegulatedAccess</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isReversible" class="member-name-link"><code>isReversible</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isShoulder" class="member-name-link"><code>isShoulder</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isSlow" class="member-name-link"><code>isSlow</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isTruckParking" class="member-name-link"><code>isTruckParking</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isTurn" class="member-name-link"><code>isTurn</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype#isVariableDriving" class="member-name-link"><code>isVariableDriving</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.

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

      LaneType (boolean isRegular,
       boolean isHighOccupancyVehicle,
       boolean isReversible,
       boolean isExpress,
       boolean isAcceleration,
       boolean isDeceleration,
       boolean isAuxiliary,
       boolean isSlow,
       boolean isPassing,
       boolean isShoulder,
       boolean isRegulatedAccess,
       boolean isTurn,
       boolean isCenterTurn,
       boolean isTruckParking,
       boolean isParking,
       boolean isVariableDriving,
       boolean isBicycle)

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

  - <div id="sdk-for-android-navigate-isRegular" class="section detail">

    ### isRegular

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRegular</span>

    </div>

    <div class="block">

    Regular lane is a lane that does not have a specific use.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isHighOccupancyVehicle" class="section detail">

    ### isHighOccupancyVehicle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHighOccupancyVehicle</span>

    </div>

    <div class="block">

    A lane which is restricted for high occupancy vehicles. Note: High occupancy vehicles are vehicles with a driver and one or more passengers.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isReversible" class="section detail">

    ### isReversible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReversible</span>

    </div>

    <div class="block">

    A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isExpress" class="section detail">

    ### isExpress

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExpress</span>

    </div>

    <div class="block">

    Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city. An express lane can be reversible, bidirectional, or one-way.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isAcceleration" class="section detail">

    ### isAcceleration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAcceleration</span>

    </div>

    <div class="block">

    An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic. These lanes can be accessed from ramps, rest areas, or weigh stations.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isDeceleration" class="section detail">

    ### isDeceleration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDeceleration</span>

    </div>

    <div class="block">

    A deceleration lane is the same as an acceleration lane but used for the opposite scenario.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isAuxiliary" class="section detail">

    ### isAuxiliary

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAuxiliary</span>

    </div>

    <div class="block">

    An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isSlow" class="section detail">

    ### isSlow

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSlow</span>

    </div>

    <div class="block">

    A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isPassing" class="section detail">

    ### isPassing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPassing</span>

    </div>

    <div class="block">

    A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass slow moving vehicles.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isShoulder" class="section detail">

    ### isShoulder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShoulder</span>

    </div>

    <div class="block">

    A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isRegulatedAccess" class="section detail">

    ### isRegulatedAccess

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRegulatedAccess</span>

    </div>

    <div class="block">

    A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals. Regulated lane access is only coded for truck holding zones that are used to regulate truck access into tunnels and over bridges using time intervals (e.g., some tunnel accesses in Switzerland).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTurn" class="section detail">

    ### isTurn

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTurn</span>

    </div>

    <div class="block">

    Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isCenterTurn" class="section detail">

    ### isCenterTurn

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCenterTurn</span>

    </div>

    <div class="block">

    Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTruckParking" class="section detail">

    ### isTruckParking

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTruckParking</span>

    </div>

    <div class="block">

    Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isParking" class="section detail">

    ### isParking

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParking</span>

    </div>

    <div class="block">

    Parking lanes are portions of the road bed that may be used for parking legally. They may allow vehicles to use them as driving lanes at times, though.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isVariableDriving" class="section detail">

    ### isVariableDriving

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVariableDriving</span>

    </div>

    <div class="block">

    Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isBicycle" class="section detail">

    ### isBicycle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBicycle</span>

    </div>

    <div class="block">

    Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean-boolean" class="section detail">

    ### LaneType

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LaneType</span><wbr></wbr><span class="parameters">(boolean isRegular, boolean isHighOccupancyVehicle, boolean isReversible, boolean isExpress, boolean isAcceleration, boolean isDeceleration, boolean isAuxiliary, boolean isSlow, boolean isPassing, boolean isShoulder, boolean isRegulatedAccess, boolean isTurn, boolean isCenterTurn, boolean isTruckParking, boolean isParking, boolean isVariableDriving, boolean isBicycle)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `isRegular` -

    Regular lane is a lane that does not have a specific use.

    `isHighOccupancyVehicle` -

    A lane which is restricted for high occupancy vehicles. Note: High occupancy vehicles are vehicles with a driver and one or more passengers.

    `isReversible` -

    A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.

    `isExpress` -

    Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city. An express lane can be reversible, bidirectional, or one-way.

    `isAcceleration` -

    An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic. These lanes can be accessed from ramps, rest areas, or weigh stations.

    `isDeceleration` -

    A deceleration lane is the same as an acceleration lane but used for the opposite scenario.

    `isAuxiliary` -

    An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.

    `isSlow` -

    A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.

    `isPassing` -

    A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass slow moving vehicles.

    `isShoulder` -

    A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.

    `isRegulatedAccess` -

    A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals. Regulated lane access is only coded for truck holding zones that are used to regulate truck access into tunnels and over bridges using time intervals (e.g., some tunnel accesses in Switzerland).

    `isTurn` -

    Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.

    `isCenterTurn` -

    Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).

    `isTruckParking` -

    Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.

    `isParking` -

    Parking lanes are portions of the road bed that may be used for parking legally. They may allow vehicles to use them as driving lanes at times, though.

    `isVariableDriving` -

    Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.

    `isBicycle` -

    Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

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

