---
title: "MapCameraAnimation.InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapCameraAnimation.InstantiationErrorCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapCameraAnimation.InstantiationErrorCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapCameraAnimation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapCameraAnimation.InstantiationErrorCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
Describes a reason for failing to create a multi-track [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview").

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK](#CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK)

Camera's look-at distance is already modified by an earlier track that modifies camera's orientation.

[CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK](#CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK)

Camera's look-at distance is already modified by an earlier track that modifies camera's position.

[CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK](#CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK)

Camera's look-at orientation is already modified by an earlier track that modifies camera's orientation.

[CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK](#CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK)

Camera's look-at orientation is already modified by an earlier track that modifies camera's position.

[CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK](#CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK)

Camera's look-at target is already modified by an earlier track that modifies camera's orientation.

[CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK](#CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK)

Camera's look-at target is already modified by an earlier track that modifies camera's position.

[CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK](#CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK)

Camera's orientation is already modified by an earlier track that modifies camera's look-at distance.

[CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK](#CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK)

Camera's orientation is already modified by an earlier track that modifies camera's look-at orientation.

[CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK](#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK)

Camera's position is already modified by an earlier track that modifies camera's look-at distance.

[CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK](#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK)

Camera's position is already modified by an earlier track that modifies camera's look-at orientation.

[CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK](#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK)

Camera's position is already modified by an earlier track that modifies camera's look-at target.

[EMPTY_TRACK_LIST](#EMPTY_TRACK_LIST)

List of keyframe tracks is empty.

[MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS](#MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS)

List of keyframe tracks contains multiple camera field-of-view tracks.

[MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS](#MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS)

List of keyframe tracks contains multiple camera focal length tracks.

[MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS](#MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS)

List of keyframe tracks contains multiple camera look-at distance tracks.

[MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS](#MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS)

List of keyframe tracks contains multiple camera look-at orientation tracks.

[MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS](#MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS)

List of keyframe tracks contains multiple camera look-at target tracks.

[MULTIPLE_CAMERA_ORIENTATION_TRACKS](#MULTIPLE_CAMERA_ORIENTATION_TRACKS)

List of keyframe tracks contains multiple camera orientation tracks.

[MULTIPLE_CAMERA_POSITION_TRACKS](#MULTIPLE_CAMERA_POSITION_TRACKS)

List of keyframe tracks contains multiple camera position tracks.

[MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS](#MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS)

List of keyframe tracks contains multiple camera principal point tracks.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapCameraAnimation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapCameraAnimation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### EMPTY_TRACK_LIST

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") EMPTY_TRACK_LIST

    List of keyframe tracks is empty.

### MULTIPLE_CAMERA_POSITION_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_POSITION_TRACKS

    List of keyframe tracks contains multiple camera position tracks.

### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK

    Camera's position is already modified by an earlier track that modifies camera's look-at target.

### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

    Camera's position is already modified by an earlier track that modifies camera's look-at orientation.

### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

    Camera's position is already modified by an earlier track that modifies camera's look-at distance.

### MULTIPLE_CAMERA_ORIENTATION_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_ORIENTATION_TRACKS

    List of keyframe tracks contains multiple camera orientation tracks.

### CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

    Camera's orientation is already modified by an earlier track that modifies camera's look-at orientation.

### CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

    Camera's orientation is already modified by an earlier track that modifies camera's look-at distance.

### MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS

    List of keyframe tracks contains multiple camera look-at target tracks.

### CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK

    Camera's look-at target is already modified by an earlier track that modifies camera's position.

### CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    Camera's look-at target is already modified by an earlier track that modifies camera's orientation.

### MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS

    List of keyframe tracks contains multiple camera look-at orientation tracks.

### CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK

    Camera's look-at orientation is already modified by an earlier track that modifies camera's position.

### CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    Camera's look-at orientation is already modified by an earlier track that modifies camera's orientation.

### MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS

    List of keyframe tracks contains multiple camera look-at distance tracks.

### CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK

    Camera's look-at distance is already modified by an earlier track that modifies camera's position.

### CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    Camera's look-at distance is already modified by an earlier track that modifies camera's orientation.

### MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS

    List of keyframe tracks contains multiple camera field-of-view tracks.

### MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS

    List of keyframe tracks contains multiple camera focal length tracks.

### MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS

public static final [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS

    List of keyframe tracks contains multiple camera principal point tracks.

## Method Details

### values

public static [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
