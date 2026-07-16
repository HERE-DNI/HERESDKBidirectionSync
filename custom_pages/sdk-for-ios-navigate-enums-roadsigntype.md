---
title: "RoadSignType Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-roadsigntype"
---

# RoadSignType

<div class="declaration">

<div class="language">

``` highlight
public enum RoadSignType : UInt32, CaseIterable, Codable
```

</div>

</div>

A road sign type classifying road signs that can appear along a road. Some signs are standardized and look the same in all countries, e.g. <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO04stopC0yA2CmF">`RoadSignType.stopSign`</a>. In general, the visual appearance of the road signs can differ across countries. Some road signs can be combined with other signs, like <a href="sdk-for-ios-navigate-enums-weathertype">`WeatherType`</a> signs. The road sign will be always shown topmost.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO7unknownyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-unknown" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO7unknownyA2CmF" class="token"><code>unknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unknown road sign type

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO19startOfNoOvertakingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-startOfNoOvertaking" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO19startOfNoOvertakingyA2CmF" class="token"><code>startOfNoOvertaking</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the starting of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#No_overtaking_or_passing_signs">Start of no overtaking sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case startOfNoOvertaking
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO17endOfNoOvertakingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-endOfNoOvertaking" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO17endOfNoOvertakingyA2CmF" class="token"><code>endOfNoOvertaking</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the ending of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#End_of_overtaking_signs">End of no overtaking sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case endOfNoOvertaking
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO28protectedOvertakingExtraLaneyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-protectedOvertakingExtraLane" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO28protectedOvertakingExtraLaneyA2CmF" class="token"><code>protectedOvertakingExtraLane</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating an extra lane for overtaking. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-3.svg">Protected overtaking extra lane sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case protectedOvertakingExtraLane
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO37protectedOvertakingExtraLaneRightSideyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-protectedOvertakingExtraLaneRightSide" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO37protectedOvertakingExtraLaneRightSideyA2CmF" class="token"><code>protectedOvertakingExtraLaneRightSide</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating an extra lane for overtaking on the right side. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-16.svg">Protected overtaking extra lane on the right side sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case protectedOvertakingExtraLaneRightSide
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO36protectedOvertakingExtraLaneLeftSideyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-protectedOvertakingExtraLaneLeftSide" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO36protectedOvertakingExtraLaneLeftSideyA2CmF" class="token"><code>protectedOvertakingExtraLaneLeftSide</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating an extra lane for overtaking on the left side. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_R6-29.svg">Protected overtaking extra lane on the left side sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case protectedOvertakingExtraLaneLeftSide
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14laneMergeRightyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-laneMergeRight" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14laneMergeRightyA2CmF" class="token"><code>laneMergeRight</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating merging of the right lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W4-3R.svg">Merge right lane sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case laneMergeRight
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13laneMergeLeftyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-laneMergeLeft" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13laneMergeLeftyA2CmF" class="token"><code>laneMergeLeft</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating merging of the left lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Mauritius#/media/File:Mauritius_Road_Signs_-_Warning_Sign_-_Traffic_Merging_From_Left_Behind.svg">Merge left lane sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case laneMergeLeft
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15laneMergeCenteryA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-laneMergeCenter" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15laneMergeCenteryA2CmF" class="token"><code>laneMergeCenter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating merging of the center lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:Roadsign_lane_drop_ahead.svg">Merge center lane sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case laneMergeCenter
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO24railwayCrossingProtectedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-railwayCrossingProtected" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO24railwayCrossingProtectedyA2CmF" class="token"><code>railwayCrossingProtected</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a protected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-4.svg">Protected railway crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case railwayCrossingProtected
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO26railwayCrossingUnprotectedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-railwayCrossingUnprotected" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO26railwayCrossingUnprotectedyA2CmF" class="token"><code>railwayCrossingUnprotected</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating an unprotected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-7-L.svg">Protected railway crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case railwayCrossingUnprotected
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11roadNarrowsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-roadNarrows" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11roadNarrowsyA2CmF" class="token"><code>roadNarrows</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a narrowing road. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W4-3.svg">Road narrows sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case roadNarrows
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14sharpCurveLeftyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sharpCurveLeft" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14sharpCurveLeftyA2CmF" class="token"><code>sharpCurveLeft</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a sharp curve to the left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512L.svg">Sharp curve left sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sharpCurveLeft
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15sharpCurveRightyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sharpCurveRight" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15sharpCurveRightyA2CmF" class="token"><code>sharpCurveRight</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a sharp curve to the right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512.svg">Sharp curve right sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sharpCurveRight
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO07windingB12StartingLeftyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-windingRoadStartingLeft" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO07windingB12StartingLeftyA2CmF" class="token"><code>windingRoadStartingLeft</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a winding road starting left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513.svg">Winding road starting left sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case windingRoadStartingLeft
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO07windingB13StartingRightyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-windingRoadStartingRight" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO07windingB13StartingRightyA2CmF" class="token"><code>windingRoadStartingRight</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a winding road starting right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513R.svg">Winding road starting right sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case windingRoadStartingRight
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO25startOfNoOvertakingTrucksyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-startOfNoOvertakingTrucks" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO25startOfNoOvertakingTrucksyA2CmF" class="token"><code>startOfNoOvertakingTrucks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no overtaking trucks. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4c.svg">No overtaking trucks sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case startOfNoOvertakingTrucks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO23endOfNoOvertakingTrucksyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-endOfNoOvertakingTrucks" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO23endOfNoOvertakingTrucksyA2CmF" class="token"><code>endOfNoOvertakingTrucks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the end of no overtaking trucks zone. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4d.svg">End of no overtaking trucks sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case endOfNoOvertakingTrucks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO16steepHillUpwardsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-steepHillUpwards" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO16steepHillUpwardsyA2CmF" class="token"><code>steepHillUpwards</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a steep hill upwards. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(b">Steep hills upwards sign</a>.svg)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case steepHillUpwards
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18steepHillDownwardsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-steepHillDownwards" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18steepHillDownwardsyA2CmF" class="token"><code>steepHillDownwards</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a steep hill downward. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(a">Steep hills downwards sign</a>.svg)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case steepHillDownwards
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO04stopC0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-stopSign" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO04stopC0yA2CmF" class="token"><code>stopSign</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a stop. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_RUS-027.svg">Stop sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case stopSign
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11lateralWindyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-lateralWind" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11lateralWindyA2CmF" class="token"><code>lateralWind</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating lateral winds. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-226.svg">Lateral winds sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case lateralWind
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO014generalWarningC0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-generalWarningSign" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO014generalWarningC0yA2CmF" class="token"><code>generalWarningSign</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a general warning. Example: <a href="https://en.wikipedia.org/wiki/File:Hong_Kong_road_sign_240.svg">General warning sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case generalWarningSign
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15riskOfGroundingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-riskOfGrounding" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15riskOfGroundingyA2CmF" class="token"><code>riskOfGrounding</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating risk of grounding. Example: <a href="https://en.wikipedia.org/wiki/File:Croatia_road_sign_A31.svg">Risk of grounding sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case riskOfGrounding
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12generalCurveyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-generalCurve" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12generalCurveyA2CmF" class="token"><code>generalCurve</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a general curve. Example: <a href="https://en.wikipedia.org/wiki/File:Italian_traffic_signs_-_curva_pericolosa_a_sinistra.svg">General curve sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case generalCurve
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO20endOfAllRestrictionsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-endOfAllRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO20endOfAllRestrictionsyA2CmF" class="token"><code>endOfAllRestrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the end of all restrictions. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_374.svg">End of all restrictions sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case endOfAllRestrictions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11generalHillyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-generalHill" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11generalHillyA2CmF" class="token"><code>generalHill</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a general hill. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W7-1A.svg">General hill sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case generalHill
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14animalCrossingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-animalCrossing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14animalCrossingyA2CmF" class="token"><code>animalCrossing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating animal crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_13b.svg">Animal crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case animalCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13icyConditionsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-icyConditions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13icyConditionsyA2CmF" class="token"><code>icyConditions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating icy conditions. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-185.png">Icy conditions sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case icyConditions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO08slipperyB0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-slipperyRoad" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO08slipperyB0yA2CmF" class="token"><code>slipperyRoad</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating slippery road. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-12.svg">Slippery road sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case slipperyRoad
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12fallingRocksyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-fallingRocks" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12fallingRocksyA2CmF" class="token"><code>fallingRocks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating falling rocks. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_1.25.2.svg">Falling rocks sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case fallingRocks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10schoolZoneyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-schoolZone" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10schoolZoneyA2CmF" class="token"><code>schoolZone</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating school zone. Example: <a href="https://en.wikipedia.org/wiki/File:Mauritius_Road_Signs_-_Warning_Sign_-_Children.svg">School zone sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case schoolZone
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15tramwayCrossingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-tramwayCrossing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15tramwayCrossingyA2CmF" class="token"><code>tramwayCrossing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a tramway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-41.svg">Tramway crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tramwayCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO16congestionHazardyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-congestionHazard" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO16congestionHazardyA2CmF" class="token"><code>congestionHazard</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating congestion hazard. Example: <a href="https://en.wikipedia.org/wiki/File:Czech_Republic_road_sign_A_23.svg">Congestion hazard sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case congestionHazard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14accidentHazardyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-accidentHazard" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO14accidentHazardyA2CmF" class="token"><code>accidentHazard</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating accident hazard. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AK31.svg">Accident hazard sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case accidentHazard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO27priorityOverOncomingTrafficyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-priorityOverOncomingTraffic" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO27priorityOverOncomingTrafficyA2CmF" class="token"><code>priorityOverOncomingTraffic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating priority over oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Zeichen_308_-_Vorrang_vor_dem_Gegenverkehr,_StVO_1992.svg">Priority over oncoming traffic sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case priorityOverOncomingTraffic
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO22yieldToOncomingTrafficyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-yieldToOncomingTraffic" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO22yieldToOncomingTrafficyA2CmF" class="token"><code>yieldToOncomingTraffic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating yielding to oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_2.5.svg">Yield to oncoming traffic sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case yieldToOncomingTraffic
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO32crossingWithPriorityFromTheRightyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-crossingWithPriorityFromTheRight" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO32crossingWithPriorityFromTheRightyA2CmF" class="token"><code>crossingWithPriorityFromTheRight</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating crossing with priority from the right. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AB1.svg">Crossing with priority from the right sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case crossingWithPriorityFromTheRight
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18pedestrianCrossingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-pedestrianCrossing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18pedestrianCrossingyA2CmF" class="token"><code>pedestrianCrossing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating pedestrian crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_171.svg">Pedestrian crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case pedestrianCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO5yieldyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-yield" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO5yieldyA2CmF" class="token"><code>yield</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating yielding. Example: <a href="https://en.wikipedia.org/wiki/File:Ontario_Wb-1A.svg">Yield sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case yield
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13doubleHairpinyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-doubleHairpin" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13doubleHairpinyA2CmF" class="token"><code>doubleHairpin</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a double hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_W1-7-L.svg">Double hairpin sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case doubleHairpin
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13tripleHairpinyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-tripleHairpin" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13tripleHairpinyA2CmF" class="token"><code>tripleHairpin</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a triple hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_doppia_curva_sx.svg">Triple hairpin sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tripleHairpin
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10embankmentyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-embankment" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10embankmentyA2CmF" class="token"><code>embankment</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating embankment. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-138.png">Embankment sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case embankment
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13twoWayTrafficyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-twoWayTraffic" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13twoWayTrafficyA2CmF" class="token"><code>twoWayTraffic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating two way traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_14.svg">Two way traffic sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case twoWayTraffic
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO9urbanAreayA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-urbanArea" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO9urbanAreayA2CmF" class="token"><code>urbanArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating urban area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_preavviso_intersezione.svg">Urban area sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case urbanArea
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10humpBridgeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-humpBridge" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO10humpBridgeyA2CmF" class="token"><code>humpBridge</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a hump bridge. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_528.svg">Hump bridge sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case humpBridge
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO06unevenB0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-unevenRoad" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO06unevenB0yA2CmF" class="token"><code>unevenRoad</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating uneven road. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_W-133.svg">Uneven road sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unevenRoad
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO9floodAreayA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-floodArea" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO9floodAreayA2CmF" class="token"><code>floodArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating a flood area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_zona_soggetta_ad_allagamento.svg">Flood area sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case floodArea
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO8obstacleyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-obstacle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO8obstacleyA2CmF" class="token"><code>obstacle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating an obstacle. Example: <a href="https://en.wikipedia.org/wiki/Warning_sign#/media/File:Belgian_road_sign_A51.svg">Obstacle sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case obstacle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO04hornC0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-hornSign" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO04hornC0yA2CmF" class="token"><code>hornSign</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating restriction for horning. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-355.png">Horn sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case hornSign
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13noEngineBrakeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noEngineBrake" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13noEngineBrakeyA2CmF" class="token"><code>noEngineBrake</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no engine brake. Example: <a href="https://commons.wikimedia.org/wiki/File:Canada_Avoid_Engine_Brake_Sign.svg">No engine brake sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noEngineBrake
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18endOfNoEngineBrakeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-endOfNoEngineBrake" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18endOfNoEngineBrakeyA2CmF" class="token"><code>endOfNoEngineBrake</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the end of no engine brake zone. Example: No examples available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case endOfNoEngineBrake
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO8noIdlingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noIdling" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO8noIdlingyA2CmF" class="token"><code>noIdling</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no idling. Example: <a href="https://en.wikipedia.org/wiki/Idle_reduction#/media/File:Idle_free_zone_-_turn_engine_off_sign.jpg">No idling sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noIdling
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13truckRolloveryA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-truckRollover" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13truckRolloveryA2CmF" class="token"><code>truckRollover</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating truck rollover. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W1-13L.svg">Truck rollover sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truckRollover
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO7lowGearyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-lowGear" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO7lowGearyA2CmF" class="token"><code>lowGear</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the use of low gear. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_Philippines#/media/File:Philippines_road_sign_S1-3.svg">Low gear sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case lowGear
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12endOfLowGearyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-endOfLowGear" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12endOfLowGearyA2CmF" class="token"><code>endOfLowGear</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating the use of low gear. Example: No examples available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case endOfLowGear
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15bicycleCrossingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-bicycleCrossing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15bicycleCrossingyA2CmF" class="token"><code>bicycleCrossing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating bicycles crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W6-7-FYG.svg">Bicycle crossing sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case bicycleCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15yieldToBicyclesyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-yieldToBicycles" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO15yieldToBicyclesyA2CmF" class="token"><code>yieldToBicycles</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating yielding to bicycles. Example: <a href="https://en.wikipedia.org/wiki/File:MK_road_sign_302.2.svg">Yield to bicycles sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case yieldToBicycles
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO21noTowedCaravanAllowedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noTowedCaravanAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO21noTowedCaravanAllowedyA2CmF" class="token"><code>noTowedCaravanAllowed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no towed caravan allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_622.7.svg">No towed caravan allowed sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noTowedCaravanAllowed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO21noTowedTrailerAllowedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noTowedTrailerAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO21noTowedTrailerAllowedyA2CmF" class="token"><code>noTowedTrailerAllowed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no towed trailer allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Sweden#/media/File:Sweden_road_sign_C6.svg">No towed trailer allowed sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noTowedTrailerAllowed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO26noCamperOrMotorhomeAllowedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noCamperOrMotorhomeAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO26noCamperOrMotorhomeAllowedyA2CmF" class="token"><code>noCamperOrMotorhomeAllowed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no camper or motorhome allowed. Example: No examples available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noCamperOrMotorhomeAllowed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11noTurnOnRedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noTurnOnRed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO11noTurnOnRedyA2CmF" class="token"><code>noTurnOnRed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating no turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:CA-QC_road_sign_P-115-1.svg">No turn on red sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noTurnOnRed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18turnPermittedOnRedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-turnPermittedOnRed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO18turnPermittedOnRedyA2CmF" class="token"><code>turnPermittedOnRed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:Chile_road_sign_RA-2.svg">Turn permitted on red sign</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case turnPermittedOnRed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12twoStageLeftyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-twoStageLeft" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO12twoStageLeftyA2CmF" class="token"><code>twoStageLeft</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating that turning left requires a two-stage maneuver, also known as a hook turn or Copenhagen Left, which is a special maneuver to safely make a left turn at an intersection without crossing oncoming traffic. This maneuver applies only in right-hand driving countries and is particularly beneficial for cyclists, as it minimizes interaction with oncoming traffic, allowing for safer crossings. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage left turn</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case twoStageLeft
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13twoStageRightyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-twoStageRight" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-roadsigntype#sdk-for-ios-navigate-s-7heresdk12RoadSignTypeO13twoStageRightyA2CmF" class="token"><code>twoStageRight</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A sign indicating turning right with the specified vehicle type requires a two stage maneuver. A TWO_STAGE_RIGHT maneuver, is a special maneuver commonly used by cyclists to safely make a right turn at an intersection without crossing oncoming traffic. This maneuver is applicable only in left-hand driving countries and is particularly beneficial for cyclists as they allow for safer crossings by minimizing the interaction with oncoming traffic. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage right turn</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case twoStageRight
  ```

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

