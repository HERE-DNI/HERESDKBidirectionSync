---
title: "InstantiationErrorCode Enumeration Reference"
slug: "sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode"
---

# InstantiationErrorCode

<div class="declaration">

<div class="language">

``` highlight
public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
```

``` highlight
extension MapCameraAnimation.InstantiationErrorCode : Error
```

</div>

Related types:

- <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>

</div>

Describes a reason for failing to create a multi-track <a href="sdk-for-ios-explore-classes-mapcameraanimation">`MapCameraAnimation`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO14emptyTrackListyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-emptyTrackList" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO14emptyTrackListyA2EmF" class="token"><code>emptyTrackList</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case emptyTrackList = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC14PositionTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraPositionTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC14PositionTracksyA2EmF" class="token"><code>multipleCameraPositionTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera position tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraPositionTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC17LookatTargetTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraPositionModifiedByCameraLookatTargetTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC17LookatTargetTrackyA2EmF" class="token"><code>cameraPositionModifiedByCameraLookatTargetTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s position is already modified by an earlier track that modifies camera’s look-at target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraPositionModifiedByCameraLookatTargetTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC22LookatOrientationTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraPositionModifiedByCameraLookatOrientationTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC22LookatOrientationTrackyA2EmF" class="token"><code>cameraPositionModifiedByCameraLookatOrientationTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s position is already modified by an earlier track that modifies camera’s look-at orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraPositionModifiedByCameraLookatOrientationTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC19LookatDistanceTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraPositionModifiedByCameraLookatDistanceTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC19LookatDistanceTrackyA2EmF" class="token"><code>cameraPositionModifiedByCameraLookatDistanceTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s position is already modified by an earlier track that modifies camera’s look-at distance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraPositionModifiedByCameraLookatDistanceTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17OrientationTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraOrientationTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17OrientationTracksyA2EmF" class="token"><code>multipleCameraOrientationTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera orientation tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraOrientationTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByc6LookatI5TrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraOrientationModifiedByCameraLookatOrientationTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByc6LookatI5TrackyA2EmF" class="token"><code>cameraOrientationModifiedByCameraLookatOrientationTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s orientation is already modified by an earlier track that modifies camera’s look-at orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraOrientationModifiedByCameraLookatOrientationTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByC19LookatDistanceTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraOrientationModifiedByCameraLookatDistanceTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByC19LookatDistanceTrackyA2EmF" class="token"><code>cameraOrientationModifiedByCameraLookatDistanceTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s orientation is already modified by an earlier track that modifies camera’s look-at distance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraOrientationModifiedByCameraLookatDistanceTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC18LookatTargetTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraLookatTargetTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC18LookatTargetTracksyA2EmF" class="token"><code>multipleCameraLookatTargetTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera look-at target tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraLookatTargetTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC13PositionTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatTargetModifiedByCameraPositionTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC13PositionTrackyA2EmF" class="token"><code>cameraLookatTargetModifiedByCameraPositionTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at target is already modified by an earlier track that modifies camera’s position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatTargetModifiedByCameraPositionTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC16OrientationTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatTargetModifiedByCameraOrientationTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC16OrientationTrackyA2EmF" class="token"><code>cameraLookatTargetModifiedByCameraOrientationTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at target is already modified by an earlier track that modifies camera’s orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatTargetModifiedByCameraOrientationTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC23LookatOrientationTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraLookatOrientationTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC23LookatOrientationTracksyA2EmF" class="token"><code>multipleCameraLookatOrientationTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera look-at orientation tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraLookatOrientationTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedByC13PositionTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatOrientationModifiedByCameraPositionTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedByC13PositionTrackyA2EmF" class="token"><code>cameraLookatOrientationModifiedByCameraPositionTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at orientation is already modified by an earlier track that modifies camera’s position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatOrientationModifiedByCameraPositionTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedBycJ5TrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatOrientationModifiedByCameraOrientationTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedBycJ5TrackyA2EmF" class="token"><code>cameraLookatOrientationModifiedByCameraOrientationTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at orientation is already modified by an earlier track that modifies camera’s orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatOrientationModifiedByCameraOrientationTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20LookatDistanceTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraLookatDistanceTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20LookatDistanceTracksyA2EmF" class="token"><code>multipleCameraLookatDistanceTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera look-at distance tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraLookatDistanceTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC13PositionTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatDistanceModifiedByCameraPositionTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC13PositionTrackyA2EmF" class="token"><code>cameraLookatDistanceModifiedByCameraPositionTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at distance is already modified by an earlier track that modifies camera’s position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatDistanceModifiedByCameraPositionTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC16OrientationTrackyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cameraLookatDistanceModifiedByCameraOrientationTrack" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC16OrientationTrackyA2EmF" class="token"><code>cameraLookatDistanceModifiedByCameraOrientationTrack</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s look-at distance is already modified by an earlier track that modifies camera’s orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cameraLookatDistanceModifiedByCameraOrientationTrack
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FieldOfViewTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraFieldOfViewTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FieldOfViewTracksyA2EmF" class="token"><code>multipleCameraFieldOfViewTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera field-of-view tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraFieldOfViewTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FocalLengthTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraFocalLengthTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FocalLengthTracksyA2EmF" class="token"><code>multipleCameraFocalLengthTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera focal length tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraFocalLengthTracks
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20PrincipalPointTracksyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-multipleCameraPrincipalPointTracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode#sdk-for-ios-explore-s-7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20PrincipalPointTracksyA2EmF" class="token"><code>multipleCameraPrincipalPointTracks</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of keyframe tracks contains multiple camera principal point tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case multipleCameraPrincipalPointTracks
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

