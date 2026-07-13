---
title: "setWarningNotificationDistances method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

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

Sets the warning notification distances for the specified warning type.

**Note**: <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> is not a valid value for this method. Use <a href="sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances">WarnerEngine.setCustomWarningNotificationDistances</a> to configure distances for a specific custom warning type.

- `warningType` The warning type for which the warning notification distances will be set. Must not be <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>.

- `warningNotificationDistances` The warning notification distances to be set for the specified warning type.

Returns `bool`. True if the distances were successfully set; false if `WarnerEngine.setWarningNotificationDistances.warningType` is <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> or the options could not be applied.

</div>

## Implementation

``` dart
bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

