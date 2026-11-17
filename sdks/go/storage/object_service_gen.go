package storage

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ObjectsService struct {
	client *conjoin.Client
}

func (s *ObjectsService) CreateUploadSignedUrl(ctx context.Context, containerNameOrID string, body *CreateUploadSignedUrlRequest, opts ...conjoin.CallOption) (*CreateUploadSignedUrlResponse, error) {
	var out CreateUploadSignedUrlResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-object/{container_name_or_id}/signed-url/upload",
		PathParams:            []string{containerNameOrID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) CreateDownloadSignedUrl(ctx context.Context, containerNameOrID string, body *CreateDownloadSignedUrlRequest, opts ...conjoin.CallOption) (*CreateDownloadSignedUrlResponse, error) {
	var out CreateDownloadSignedUrlResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-object/{container_name_or_id}/signed-url/download",
		PathParams:            []string{containerNameOrID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) Rename(ctx context.Context, containerNameOrID string, oldName string, newName string, opts ...conjoin.CallOption) (*RenameObjectResponse, error) {
	var out RenameObjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-object/rename/{container_name_or_id}/{old_name}/{new_name}",
		PathParams: []string{containerNameOrID, oldName, newName},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) Archive(ctx context.Context, containerNameOrID string, objectNameOrID string, opts ...conjoin.CallOption) (*ArchiveObjectResponse, error) {
	var out ArchiveObjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-object/archive/{container_name_or_id}/{object_name_or_id}",
		PathParams: []string{containerNameOrID, objectNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) Restore(ctx context.Context, containerNameOrID string, objectNameOrID string, opts ...conjoin.CallOption) (*RestoreObjectResponse, error) {
	var out RestoreObjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "storage/storage-object/restore/{container_name_or_id}/{object_name_or_id}",
		PathParams: []string{containerNameOrID, objectNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) Delete(ctx context.Context, containerNameOrID string, prefix string, name string, opts ...conjoin.CallOption) (*DeleteObjectResponse, error) {
	var out DeleteObjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "storage/storage-object/{container_name_or_id}/{prefix}/{name}",
		PathParams: []string{containerNameOrID, prefix, name},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) ListVersions(ctx context.Context, containerNameOrID string, objectNameOrID string, query *ListObjectVersionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListObjectVersionsItem], error) {
	return conjoin.List[ListObjectVersionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "storage/storage-object/versions/{container_name_or_id}/{object_name_or_id}",
		PathParams: []string{containerNameOrID, objectNameOrID},
		Query:      query,
	}, opts...)
}

func (s *ObjectsService) RestoreVersion(ctx context.Context, containerNameOrID string, objectNameOrID string, body *RestoreObjectVersionRequest, opts ...conjoin.CallOption) (*RestoreObjectVersionResponse, error) {
	var out RestoreObjectVersionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "storage/storage-object/versions/restore/{container_name_or_id}/{object_name_or_id}",
		PathParams:            []string{containerNameOrID, objectNameOrID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) CheckDuplicate(ctx context.Context, containerNameOrID string, query *CheckObjectDuplicateQuery, opts ...conjoin.CallOption) (*CheckObjectDuplicateResponse, error) {
	var out CheckObjectDuplicateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "storage/storage-object/check-duplicate/{container_name_or_id}",
		PathParams:    []string{containerNameOrID},
		Query:         query,
		QueryRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) Read(ctx context.Context, containerNameOrID string, objectNameOrID string, opts ...conjoin.CallOption) (*ReadObjectResponse, error) {
	var out ReadObjectResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "storage/storage-object/{container_name_or_id}/{object_name_or_id}",
		PathParams: []string{containerNameOrID, objectNameOrID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ObjectsService) List(ctx context.Context, containerNameOrID string, query *ListObjectsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListObjectsItem], error) {
	return conjoin.List[ListObjectsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "storage/storage-object/{container_name_or_id}",
		PathParams: []string{containerNameOrID},
		Query:      query,
	}, opts...)
}
