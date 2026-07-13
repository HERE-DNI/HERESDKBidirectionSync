---
title: "setWarningNotificationDistances method - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWarningNotificationDistances.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setWarningNotificationDistances</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">setWarningNotificationDistances</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>

)

</div>

<div class="section desc markdown">

Set the warning notification distances for the specified warning types.

**Note:** The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use `NavigatorInterface.school_zone_warning_options` instead. Attempting to set the warning notification distances for the school zone warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `SchoolZoneWarningOptions.warning_distance_in_meters` to set the warning notification distance for the school zone warner regardless of the `TimingProfile`. If `NavigatorInterface.set_warning_notification_distances` could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `TrafficMergeWarningOptions.warning_distance_in_meters` to set the warning notification distance for the traffic merge warner regardless of the `TimingProfile`. Using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false` to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.

- `warningType` The warning type for which the warning notification distances will be set.

- `warningNotificationDistances` The warning notification distances to be set for the specified warning types.

Returns `bool`. `True` if set successfully, `false` when the warning_type is `WarningType.SCHOOL_ZONE` or the options have invalid values, see <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> for more details about warning notification distances.

</div>

## Implementation

``` dart
bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
