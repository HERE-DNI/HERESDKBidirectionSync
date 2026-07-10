---
title: "ManeuverNotificationTimingOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.ManeuverNotificationTimingOptions → com.here.sdk.navigation.ManeuverNotificationTimingOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverNotificationTimingOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class defining timing and distance thresholds for maneuver notifications. Setting custom values will impact the time when the notification for each supported ManeuverNotificationType is sent - dependent on the TimingProfile . Note: By default, notification thresholds depend on TimingProfile . When custom values are set, then these rules will still apply. The following rules apply for all transport modes: For TimingProfile.FAST_SPEED timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for TimingProfile.REGULAR_SPEED timing profile will be used instead. For TimingProfile.REGULAR_SPEED timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for TimingProfile.SLOW_SPEED timing profile will be used instead. For TimingProfile.SLOW_SPEED timing profile the thresholds will be always used as specified. The timings follow a strict order: ManeuverNotificationType.RANGE : The first notification, it may be very far away (use 0 for farthest or earliest possible notification). ManeuverNotificationType.REMINDER : The second notification. ManeuverNotificationType.DISTANCE : A second reminder notification to take action. ManeuverNotificationType.ACTION : Final notification, specifying the required action to be taken. Therefore, it is crucial that the set values do not violate the order: range \> reminder \> distance \> action. For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400. If rangeNotificationDistanceInMeters is smaller than reminderNotificationDistanceInMeters the new options will be silently ignored and the previous values are kept. You always have the choice to specify the thresholds for time or distance. For each ManeuverNotificationType a notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time and distance values. A configuration value of 0 is only allowed for rangeNotificationDistanceInMeters and rangeNotificationTimeInSeconds . It means that the maneuver notifications of type ManeuverNotificationType.RANGE should be generated as soon as the maneuver location is known - no matter how far away it may be. It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above. You can also specify the doubleNotificationDistanceInMeters threshold that determines the distance between two maneuvers that should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this threshold will be merged like in this example: "After 300 meters turn right and then turn left.". Tip: To set the timings to the HERE SDK, you can first call getManeuverNotificationTimingOptions() to get the default values for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the setManeuverNotificationTimingOptions() . Note: In the comment of each attribute, the term Others refers to non-pedestrian transport modes such as TransportMode.CAR , TransportMode.BICYCLE , TransportMode.TRUCK . Attention: The default values for TransportMode.PEDESTRIAN on TimingProfile.FAST_SPEED are theoretical, as such routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians. Usage example: // Get current values or default values, if no values have been set before. ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED); // Set a new value for a specific option and keep the previous or default values for the others. car_highway_timings.distanceNotificationDistanceInMeters = 1500; // Apply the changes to Navigator (or VisualNavigator). Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);

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

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#actionNotificationDistanceInMeters" class="member-name-link"><code>actionNotificationDistanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The default distance setting for ManeuverNotificationType.ACTION notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#actionNotificationTimeInSeconds" class="member-name-link"><code>actionNotificationTimeInSeconds</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The default time setting for ManeuverNotificationType.ACTION notification.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#distanceNotificationDistanceInMeters" class="member-name-link"><code>distanceNotificationDistanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The default distance setting for ManeuverNotificationType.DISTANCE notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#distanceNotificationTimeInSeconds" class="member-name-link"><code>distanceNotificationTimeInSeconds</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The default time setting for ManeuverNotificationType.DISTANCE notification.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#doubleNotificationDistanceInMeters" class="member-name-link"><code>doubleNotificationDistanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The default distance setting for double notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters" class="member-name-link"><code>rangeNotificationDistanceInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The default distance setting for ManeuverNotificationType.RANGE notification.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds" class="member-name-link"><code>rangeNotificationTimeInSeconds</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The default time setting for ManeuverNotificationType.RANGE notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#reminderNotificationDistanceInMeters" class="member-name-link"><code>reminderNotificationDistanceInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The default distance setting for ManeuverNotificationType.REMINDER notification.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#reminderNotificationTimeInSeconds" class="member-name-link"><code>reminderNotificationTimeInSeconds</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The default time setting for ManeuverNotificationType.REMINDER notification.

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

      ManeuverNotificationTimingOptions (int rangeNotificationDistanceInMeters,
       int rangeNotificationTimeInSeconds,
       int reminderNotificationDistanceInMeters,
       int reminderNotificationTimeInSeconds,
       int distanceNotificationDistanceInMeters,
       int distanceNotificationTimeInSeconds,
       int actionNotificationDistanceInMeters,
       int actionNotificationTimeInSeconds,
       int doubleNotificationDistanceInMeters)

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

  - <div id="sdk-for-android-navigate-rangeNotificationDistanceInMeters" class="section detail">

    ### rangeNotificationDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">rangeNotificationDistanceInMeters</span>

    </div>

    <div class="block">

    The default distance setting for ManeuverNotificationType.RANGE notification. A configuration value of 0 is only allowed for rangeNotificationDistanceInMeters and rangeNotificationTimeInSeconds . It means that the maneuver notifications of type ManeuverNotificationType.RANGE should be generated as soon as the maneuver location is known - no matter how far away it may be. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 0 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 0 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 0 Others TimingProfile.FAST_SPEED 0 Others TimingProfile.REGULAR_SPEED 0 Others TimingProfile.SLOW_SPEED 0

    </div>

    </div>

  - <div id="sdk-for-android-navigate-rangeNotificationTimeInSeconds" class="section detail">

    ### rangeNotificationTimeInSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">rangeNotificationTimeInSeconds</span>

    </div>

    <div class="block">

    The default time setting for ManeuverNotificationType.RANGE notification. A configuration value of 0 is only allowed for rangeNotificationDistanceInMeters and rangeNotificationTimeInSeconds . It means that the maneuver notifications of type ManeuverNotificationType.RANGE should be generated as soon as the maneuver location is known - no matter how far away it may be. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 0 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 0 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 0 Others TimingProfile.FAST_SPEED 0 Others TimingProfile.REGULAR_SPEED 0 Others TimingProfile.SLOW_SPEED 0

    </div>

    </div>

  - <div id="sdk-for-android-navigate-reminderNotificationDistanceInMeters" class="section detail">

    ### reminderNotificationDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">reminderNotificationDistanceInMeters</span>

    </div>

    <div class="block">

    The default distance setting for ManeuverNotificationType.REMINDER notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 500 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 500 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 500 Others TimingProfile.FAST_SPEED 2300 Others TimingProfile.REGULAR_SPEED 800 Others TimingProfile.SLOW_SPEED 600

    </div>

    </div>

  - <div id="sdk-for-android-navigate-reminderNotificationTimeInSeconds" class="section detail">

    ### reminderNotificationTimeInSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">reminderNotificationTimeInSeconds</span>

    </div>

    <div class="block">

    The default time setting for ManeuverNotificationType.REMINDER notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 40 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 40 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 40 Others TimingProfile.FAST_SPEED 40 Others TimingProfile.REGULAR_SPEED 40 Others TimingProfile.SLOW_SPEED 40

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceNotificationDistanceInMeters" class="section detail">

    ### distanceNotificationDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">distanceNotificationDistanceInMeters</span>

    </div>

    <div class="block">

    The default distance setting for ManeuverNotificationType.DISTANCE notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 100 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 100 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 100 Others TimingProfile.FAST_SPEED 1300 Others TimingProfile.REGULAR_SPEED 300 Others TimingProfile.SLOW_SPEED 300

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceNotificationTimeInSeconds" class="section detail">

    ### distanceNotificationTimeInSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">distanceNotificationTimeInSeconds</span>

    </div>

    <div class="block">

    The default time setting for ManeuverNotificationType.DISTANCE notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 18 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 18 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 18 Others TimingProfile.FAST_SPEED 18 Others TimingProfile.REGULAR_SPEED 18 Others TimingProfile.SLOW_SPEED 18

    </div>

    </div>

  - <div id="sdk-for-android-navigate-actionNotificationDistanceInMeters" class="section detail">

    ### actionNotificationDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">actionNotificationDistanceInMeters</span>

    </div>

    <div class="block">

    The default distance setting for ManeuverNotificationType.ACTION notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 10 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 10 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 10 Others TimingProfile.FAST_SPEED 400 Others TimingProfile.REGULAR_SPEED 100 Others TimingProfile.SLOW_SPEED 50

    </div>

    </div>

  - <div id="sdk-for-android-navigate-actionNotificationTimeInSeconds" class="section detail">

    ### actionNotificationTimeInSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">actionNotificationTimeInSeconds</span>

    </div>

    <div class="block">

    The default time setting for ManeuverNotificationType.ACTION notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 5 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 5 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 5 Others TimingProfile.FAST_SPEED 5 Others TimingProfile.REGULAR_SPEED 5 Others TimingProfile.SLOW_SPEED 5

    </div>

    </div>

  - <div id="sdk-for-android-navigate-doubleNotificationDistanceInMeters" class="section detail">

    ### doubleNotificationDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">doubleNotificationDistanceInMeters</span>

    </div>

    <div class="block">

    The default distance setting for double notification. Transport Mode Timing Profile Default value TransportMode.PEDESTRIAN TimingProfile.FAST_SPEED 20 TransportMode.PEDESTRIAN TimingProfile.REGULAR_SPEED 20 TransportMode.PEDESTRIAN TimingProfile.SLOW_SPEED 20 Others TimingProfile.FAST_SPEED 750 Others TimingProfile.REGULAR_SPEED 250 Others TimingProfile.SLOW_SPEED 150

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-int-int-int-int-int-int-int-int-int" class="section detail">

    ### ManeuverNotificationTimingOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ManeuverNotificationTimingOptions</span><wbr></wbr><span class="parameters">(int rangeNotificationDistanceInMeters, int rangeNotificationTimeInSeconds, int reminderNotificationDistanceInMeters, int reminderNotificationTimeInSeconds, int distanceNotificationDistanceInMeters, int distanceNotificationTimeInSeconds, int actionNotificationDistanceInMeters, int actionNotificationTimeInSeconds, int doubleNotificationDistanceInMeters)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `rangeNotificationDistanceInMeters` -

    The default distance setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#RANGE">`ManeuverNotificationType.RANGE`</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters">`rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds">`rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#RANGE">`ManeuverNotificationType.RANGE`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 0 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 0 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 0 |

    </p>

    `rangeNotificationTimeInSeconds` -

    The default time setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#RANGE">`ManeuverNotificationType.RANGE`</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters">`rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds">`rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#RANGE">`ManeuverNotificationType.RANGE`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 0 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 0 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 0 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 0 |

    </p>

    `reminderNotificationDistanceInMeters` -

    The default distance setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#REMINDER">`ManeuverNotificationType.REMINDER`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 500 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 500 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 500 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 2300 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 800 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 600 |

    </p>

    `reminderNotificationTimeInSeconds` -

    The default time setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#REMINDER">`ManeuverNotificationType.REMINDER`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 40 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 40 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 40 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 40 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 40 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 40 |

    </p>

    `distanceNotificationDistanceInMeters` -

    The default distance setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#DISTANCE">`ManeuverNotificationType.DISTANCE`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 100 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 100 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 100 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 1300 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 300 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 300 |

    </p>

    `distanceNotificationTimeInSeconds` -

    The default time setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#DISTANCE">`ManeuverNotificationType.DISTANCE`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 18 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 18 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 18 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 18 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 18 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 18 |

    </p>

    `actionNotificationDistanceInMeters` -

    The default distance setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#ACTION">`ManeuverNotificationType.ACTION`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 10 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 10 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 10 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 400 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 100 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 50 |

    </p>

    `actionNotificationTimeInSeconds` -

    The default time setting for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype#ACTION">`ManeuverNotificationType.ACTION`</a> notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 5 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 5 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 5 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 5 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 5 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 5 |

    </p>

    `doubleNotificationDistanceInMeters` -

    The default distance setting for double notification.

    | Transport Mode | Timing Profile | Default value |
    |----|----|----|
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 20 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 20 |
    | <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode#PEDESTRIAN">`TransportMode.PEDESTRIAN`</a> | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 20 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#FAST_SPEED">`TimingProfile.FAST_SPEED`</a> | 750 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#REGULAR_SPEED">`TimingProfile.REGULAR_SPEED`</a> | 250 |
    | Others | <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile#SLOW_SPEED">`TimingProfile.SLOW_SPEED`</a> | 150 |

    </p>

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

