---
title: "ManeuverNotificationTimingOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions"
---

# ManeuverNotificationTimingOptions

<div class="declaration">

<div class="language">

``` highlight
public struct ManeuverNotificationTimingOptions : Hashable
```

</div>

</div>

A struct defining timing and distance thresholds for maneuver notifications.

Setting custom values will impact the time when the notification for each supported <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> is sent - dependent on the <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>.

**Note:** By default, notification thresholds depend on <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>. When custom values are set, then these rules will still apply. The following rules apply for all transport modes:

- For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> timing profile will be used instead.
- For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> timing profile will be used instead.
- For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> timing profile the thresholds will be always used as specified.

The timings follow a strict order:

1.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).
2.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a>: The second notification.
3.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a>: A second reminder notification to take action.
4.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a>: Final notification, specifying the required action to be taken.

Therefore, it is crucial that the set values do not violate the order: range \> reminder \> distance \> action. For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400. If <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> is smaller than <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters`</a> the new options will be silently ignored and the previous values are kept.

You always have the choice to specify the thresholds for time or distance. For each <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> a notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time and distance values. A configuration value of 0 is only allowed for <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be. It’s impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.

You can also specify the <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters`</a> threshold that determines the distance between two maneuvers that should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this threshold will be merged like in this example: “After 300 meters turn right and then turn left.”.

Tip: To set the timings to the HERE SDK, you can first call

    getManeuverNotificationTimingOptions()

to get the default values for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the

    setManeuverNotificationTimingOptions()

.
</p>

Note: In the comment of each attribute, the term `Others` refers to non-pedestrian transport modes such as <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO7bicycleyA2CmF">`TransportMode.bicycle`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>.

Attention: The default values for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> on <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> are theoretical, as such routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.

Usage example:

``` highlight
// Get current values or default values, if no values have been set before. ManeuverNotificationTimingOptions car_highway_timings = Navigator . getManeuverNotificationTimingOptions ( TransportMode . car , TimingProfile . FAST_SPEED ); // Set a new value for a specific option and keep the previous or default values for the others. car_highway_timings . distanceNotificationDistanceInMeters = 1500 ; // Apply the changes to Navigator (or VisualNavigator). Navigator . setManeuverNotificationTimingOptions ( TransportMode . car , TimingProfile . FAST_SPEED , car_fast_speed_timings );
```

</pre>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/rangeNotificationDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp" class="token"><code>rangeNotificationDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> notification. A configuration value of 0 is only allowed for `ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters` and <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 0 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 0 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 0 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeNotificationDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/rangeNotificationTimeInSeconds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp" class="token"><code>rangeNotificationTimeInSeconds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> and `ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 0 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 0 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 0 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 0 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeNotificationTimeInSeconds: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/reminderNotificationDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp" class="token"><code>reminderNotificationDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 500 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 500 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 500 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 2300 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 800 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 600 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var reminderNotificationDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC13TimeInSecondss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/reminderNotificationTimeInSeconds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC13TimeInSecondss5Int32Vvp" class="token"><code>reminderNotificationTimeInSeconds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 40 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 40 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 40 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 40 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 40 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 40 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var reminderNotificationTimeInSeconds: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC16DistanceInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/distanceNotificationDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC16DistanceInMeterss5Int32Vvp" class="token"><code>distanceNotificationDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 100 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 100 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 100 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 1300 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 300 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 300 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceNotificationDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC13TimeInSecondss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/distanceNotificationTimeInSeconds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC13TimeInSecondss5Int32Vvp" class="token"><code>distanceNotificationTimeInSeconds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 18 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 18 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 18 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 18 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 18 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 18 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceNotificationTimeInSeconds: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC16DistanceInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/actionNotificationDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC16DistanceInMeterss5Int32Vvp" class="token"><code>actionNotificationDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 10 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 10 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 10 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 400 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 100 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 50 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var actionNotificationDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC13TimeInSecondss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/actionNotificationTimeInSeconds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC13TimeInSecondss5Int32Vvp" class="token"><code>actionNotificationTimeInSeconds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a> notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 5 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 5 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 5 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 5 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 5 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 5 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var actionNotificationTimeInSeconds: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/doubleNotificationDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp" class="token"><code>doubleNotificationDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default distance setting for double notification.

  | Transport Mode | Timing Profile | Default value |
  |----|----|----|
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 20 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 20 |
  | <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 20 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> | 750 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> | 250 |
  | Others | <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> | 150 |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var doubleNotificationDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(rangeNotificationDistanceInMeters: rangeNotificationTimeInSeconds: reminderNotificationDistanceInMeters: reminderNotificationTimeInSeconds: distanceNotificationDistanceInMeters: distanceNotificationTimeInSeconds: actionNotificationDistanceInMeters: actionNotificationTimeInSeconds: doubleNotificationDistanceInMeters: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - rangeNotificationDistanceInMeters: The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| ——————————\| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 0 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 0 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 0 \|

    - rangeNotificationTimeInSeconds: The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| ——————————\| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 0 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 0 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 0 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 0 \|

    - reminderNotificationDistanceInMeters: The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| ——————————\| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 500 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 500 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 500 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 2300 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 800 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 600 \|

    - reminderNotificationTimeInSeconds: The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| —————————– \| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 40 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 40 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 40 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 40 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 40 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 40 \|

    - distanceNotificationDistanceInMeters: The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| —————————– \| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 100 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 100 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 100 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 1300 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 300 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 300 \|

    - distanceNotificationTimeInSeconds: The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| —————————– \| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 18 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 18 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 18 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 18 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 18 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 18 \|

    - actionNotificationDistanceInMeters: The default distance setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| ——————————\| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 10 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 10 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 10 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 400 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 100 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 50 \|

    - actionNotificationTimeInSeconds: The default time setting for <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a> notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| —————————– \| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 5 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 5 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 5 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 5 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 5 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 5 \|

    - doubleNotificationDistanceInMeters: The default distance setting for double notification.

    \| Transport Mode \| Timing Profile \| Default value \| \| —————————————- \| —————————– \| —————————————- \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 20 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 20 \| \| <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 20 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> \| 750 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> \| 250 \| \| Others \| <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> \| 150 \|

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( rangeNotificationDistanceInMeters : Int32 , rangeNotificationTimeInSeconds : Int32 , reminderNotificationDistanceInMeters : Int32 , reminderNotificationTimeInSeconds : Int32 , distanceNotificationDistanceInMeters : Int32 , distanceNotificationTimeInSeconds : Int32 , actionNotificationDistanceInMeters : Int32 , actionNotificationTimeInSeconds : Int32 , doubleNotificationDistanceInMeters : Int32 )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

