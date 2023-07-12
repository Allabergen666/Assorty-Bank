import graphene
from graphene_django import DjangoObjectType
from main.models import (Anime, Category, Contact, ContactSlider, HomeImage,
                         HomeRowText, Post, Profile)


class CategoryModelType(DjangoObjectType):
    class Meta:
        model = Category


class PostModelType(DjangoObjectType):
    class Meta:
        model = Post


class HomeImageModelType(DjangoObjectType):
    class Meta:
        model = HomeImage


class HomeRowTextModelType(DjangoObjectType):
    class Meta:
        model = HomeRowText


class ContactModelType(DjangoObjectType):
    class Meta:
        model = Contact


class ContactSliderModelType(DjangoObjectType):
    class Meta:
        model = ContactSlider


class AnimeModelType(DjangoObjectType):
    class Meta:
        model = Anime


class ProfileModelType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    category_model = graphene.List(CategoryModelType)
    post_model = graphene.List(PostModelType)
    home_image_model = graphene.List(HomeImageModelType)
    home_row_text_model = graphene.List(HomeRowTextModelType)
    contact_model = graphene.List(ContactModelType)
    contact_slider_model = graphene.List(ContactSliderModelType)
    anime_model = graphene.List(AnimeModelType)
    profile_model = graphene.List(ProfileModelType)

    def resolve_category_model(self, info, filters=None, order_by=None, first=None, skip=None):
        categories = Category.objects.all()

        if skip:
            categories = categories[skip:]

        if first:
            categories = categories[:first]

        return categories
    
    def resolve_post_model(self, info, filters=None, order_by=None, first=None, skip=None):
        posts = Post.objects.all()

        if skip:
            posts = posts[skip:]

        if first:
            posts = posts[:first]

        return posts

    def resolve_home_image_model(self, info, filters=None, order_by=None, first=None, skip=None):
        home_images = HomeImage.objects.all()

        if skip:
            home_images = home_images[skip:]

        if first:
            home_images = home_images[:first]

        return home_images
    
    def resolve_home_row_text_model(self, info, filters=None, order_by=None, first=None, skip=None):
        home_row_texts = HomeRowText.objects.all()

        if skip:
            home_row_texts = home_row_texts[skip:]

        if first:
            home_row_texts = home_row_texts[:first]

        return home_row_texts
    
    def resolve_contact_model(self, info, filters=None, order_by=None, first=None, skip=None):
        contacts = Contact.objects.all()

        if skip:
            contacts = contacts[skip:]

        if first:
            contacts = contacts[:first]

        return contacts
    
    def resolve_contact_slider_model(self, info, filters=None, order_by=None, first=None, skip=None):
        contact_sliders = ContactSlider.objects.all()

        if skip:
            contact_sliders = contact_sliders[skip:]

        if first:
            contact_sliders = contact_sliders[:first]

        return contact_sliders
    
    def resolve_anime_model(self, info, filters=None, order_by=None, first=None, skip=None):
        animes = Anime.objects.all()

        if skip:
            animes = animes[skip:]

        if first:
            animes = animes[:first]

        return animes
    
    def resolve_profile_model(self, info, filters=None, order_by=None, first=None, skip=None):
        profiles = Profile.objects.all()

        if skip:
            profiles = profiles[skip:]

        if first:
            profiles = profiles[:first]

        return profiles
    

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        # Добавьте другие аргументы, если необходимо

    category = graphene.Field(CategoryModelType)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        # Добавьте другие аргументы, если необходимо

    category = graphene.Field(CategoryModelType)

    def mutate(self, info, id, name=None):
        category = Category.objects.get(id=id)

        if name:
            category.name = name

        # Обновите другие поля, если необходимо

        category.save()
        return UpdateCategory(category=category)

class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategory(success=True)


class CreatePost(graphene.Mutation):
    class Arguments:
        image = graphene.String(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        category_id = graphene.Int(required=True)
        location = graphene.String(required=True)

    post = graphene.Field(PostModelType)

    def mutate(self, info, image, title, description, category_id, location):
        category = Category.objects.get(id=category_id)
        post = Post.objects.create(image=image, title=title, description=description, category=category, location=location)
        return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()
        title = graphene.String()
        description = graphene.String()
        category_id = graphene.Int()
        location = graphene.String()

    post = graphene.Field(PostModelType)

    def mutate(self, info, id, image=None, title=None, description=None, category_id=None, location=None):
        post = Post.objects.get(id=id)

        if image:
            post.image = image
        if title:
            post.title = title
        if description:
            post.description = description
        if category_id:
            category = Category.objects.get(id=category_id)
            post.category = category
        if location:
            post.location = location

        post.save()
        return UpdatePost(post=post)

class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        post = Post.objects.get(id=id)
        post.delete()
        return DeletePost(success=True)


class CreateHomeImage(graphene.Mutation):
    class Arguments:
        image = graphene.String(required=True)

    home_image = graphene.Field(HomeImageModelType)

    def mutate(self, info, image):
        home_image = HomeImage.objects.create(image=image)
        return CreateHomeImage(home_image=home_image)

class UpdateHomeImage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()

    home_image = graphene.Field(HomeImageModelType)

    def mutate(self, info, id, image=None):
        home_image = HomeImage.objects.get(id=id)

        if image:
            home_image.image = image

        home_image.save()
        return UpdateHomeImage(home_image=home_image)

class DeleteHomeImage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        home_image = HomeImage.objects.get(id=id)
        home_image.delete()
        return DeleteHomeImage(success=True)


class CreateHomeRowText(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    home_row_text = graphene.Field(HomeRowTextModelType)

    def mutate(self, info, title, description):
        home_row_text = HomeRowText.objects.create(title=title, description=description)
        return CreateHomeRowText(home_row_text=home_row_text)

class UpdateHomeRowText(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    home_row_text = graphene.Field(HomeRowTextModelType)

    def mutate(self, info, id, title=None, description=None):
        home_row_text = HomeRowText.objects.get(id=id)

        if title:
            home_row_text.title = title
        if description:
            home_row_text.description = description

        home_row_text.save()
        return UpdateHomeRowText(home_row_text=home_row_text)

class DeleteHomeRowText(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        home_row_text = HomeRowText.objects.get(id=id)
        home_row_text.delete()
        return DeleteHomeRowText(success=True)


class CreateContact(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        message = graphene.String(required=True)

    contact = graphene.Field(ContactModelType)

    def mutate(self, info, name, email, message):
        contact = Contact.objects.create(name=name, email=email, message=message)
        return CreateContact(contact=contact)

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        message = graphene.String()

    contact = graphene.Field(ContactModelType)

    def mutate(self, info, id, name=None, email=None, message=None):
        contact = Contact.objects.get(id=id)

        if name:
            contact.name = name
        if email:
            contact.email = email
        if message:
            contact.message = message

        contact.save()
        return UpdateContact(contact=contact)

class DeleteContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        contact = Contact.objects.get(id=id)
        contact.delete()
        return DeleteContact(success=True)


class CreateContactSlider(graphene.Mutation):
    class Arguments:
        image = graphene.String(required=True)

    contact_slider = graphene.Field(ContactSliderModelType)

    def mutate(self, info, image):
        contact_slider = ContactSlider.objects.create(image=image)
        return CreateContactSlider(contact_slider=contact_slider)

class UpdateContactSlider(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()

    contact_slider = graphene.Field(ContactSliderModelType)

    def mutate(self, info, id, image=None):
        contact_slider = ContactSlider.objects.get(id=id)

        if image:
            contact_slider.image = image

        contact_slider.save()
        return UpdateContactSlider(contact_slider=contact_slider)

class DeleteContactSlider(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        contact_slider = ContactSlider.objects.get(id=id)
        contact_slider.delete()
        return DeleteContactSlider(success=True)


class CreateAnime(graphene.Mutation):
    class Arguments:
        image = graphene.String(required=True)
        title = graphene.String(required=True)
        category = graphene.String(required=True)
        description = graphene.String(required=True)

    anime = graphene.Field(AnimeModelType)

    def mutate(self, info, image, title, category, description):
        anime = Anime.objects.create(image=image, title=title, category=category, description=description)
        return CreateAnime(anime=anime)

class UpdateAnime(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        image = graphene.String()
        title = graphene.String()
        category = graphene.String()
        description = graphene.String()

    anime = graphene.Field(AnimeModelType)

    def mutate(self, info, id, image=None, title=None, category=None, description=None):
        anime = Anime.objects.get(id=id)

        if image:
            anime.image = image
        if title:
            anime.title = title
        if category:
            anime.category = category
        if description:
            anime.description = description

        anime.save()
        return UpdateAnime(anime=anime)

class DeleteAnime(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        anime = Anime.objects.get(id=id)
        anime.delete()
        return DeleteAnime(success=True)


class CreateProfile(graphene.Mutation):
    class Arguments:
        image = graphene.String()
        phone = graphene.String()
        birth_date = graphene.Date()
        about = graphene.String()

    profile = graphene.Field(ProfileModelType)

    def mutate(self, info, image=None, phone=None, birth_date=None, about=None):
        user = info.context.user
        profile = Profile.objects.create(user=user, image=image, phone=phone, birth_date=birth_date, about=about)
        return CreateProfile(profile=profile)

class UpdateProfile(graphene.Mutation):
    class Arguments:
        image = graphene.String()
        phone = graphene.String()
        birth_date = graphene.Date()
        about = graphene.String()

    profile = graphene.Field(ProfileModelType)

    def mutate(self, info, image=None, phone=None, birth_date=None, about=None):
        user = info.context.user
        profile = user.profile

        if image:
            profile.image = image
        if phone:
            profile.phone = phone
        if birth_date:
            profile.birth_date = birth_date
        if about:
            profile.about = about

        profile.save()
        return UpdateProfile(profile=profile)

class DeleteProfile(graphene.Mutation):
    success = graphene.Boolean()

    def mutate(self, info):
        user = info.context.user
        profile = user.profile
        profile.delete()
        return DeleteProfile(success=True)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

    create_home_image = CreateHomeImage.Field()
    update_home_image = UpdateHomeImage.Field()
    delete_home_image = DeleteHomeImage.Field()

    create_home_row_text = CreateHomeRowText.Field()
    update_home_row_text = UpdateHomeRowText.Field()
    delete_home_row_text = DeleteHomeRowText.Field()

    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    delete_contact = DeleteContact.Field()

    create_contact_slider = CreateContactSlider.Field()
    update_contact_slider = UpdateContactSlider.Field()
    delete_contact_slider = DeleteContactSlider.Field()

    create_anime = CreateAnime.Field()
    update_anime = UpdateAnime.Field()
    delete_anime = DeleteAnime.Field()

    create_profile = CreateProfile.Field()
    update_profile = UpdateProfile.Field()
    delete_profile = DeleteProfile.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=True)