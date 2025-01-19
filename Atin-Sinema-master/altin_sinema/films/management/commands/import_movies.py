# import pandas as pd
# from django.core.management.base import BaseCommand
# from films.models import Movie, Category, Director, Screenwriter, Actor, Country, ProductionCompany
# # python manage.py import_movies "C:\Users\Muhammet Ali Mutlu\Desktop\movie_database.xlsx"
# # excel dosya yolu verildiğinde bu dosyadaki verileri veritabanına ekler
# class Command(BaseCommand):
#     help = "Import movies from an Excel file"

#     def add_arguments(self, parser):
#         parser.add_argument('file_path', type=str, help="Path to the Excel file")

#     def handle(self, *args, **kwargs):
#         file_path = kwargs['file_path']
#         try:
#             # Read the Excel file
#             data = pd.read_excel(file_path)

#             for _, row in data.iterrows():
#                 # Create or update the Movie instance
#                 movie, created = Movie.objects.get_or_create(
#                     original_title=row['original_title'],
#                     defaults={
#                         'title': row.get('title', ''),
#                         'imdb_score': row.get('imdb_score', 0.0),
#                         'release_year': row.get('release_year', 2000),
#                         'description': row.get('description', 'No description available'),
#                         'iframe_url': row.get('iframe_url', '<iframe></iframe>'),
#                         'duration': row.get('duration', 0),
#                     }
#                 )

#                 # Many-to-many relationships
#                 if 'categories' in row and not pd.isna(row['categories']):
#                     for category_name in row['categories'].split(','):
#                         category, _ = Category.objects.get_or_create(name=category_name.strip())
#                         movie.categories.add(category)

#                 if 'directors' in row and not pd.isna(row['directors']):
#                     for director_name in row['directors'].split(','):
#                         director, _ = Director.objects.get_or_create(name=director_name.strip())
#                         movie.directors.add(director)

#                 if 'screenwriters' in row and not pd.isna(row['screenwriters']):
#                     for screenwriter_name in row['screenwriters'].split(','):
#                         screenwriter, _ = Screenwriter.objects.get_or_create(name=screenwriter_name.strip())
#                         movie.screenwriters.add(screenwriter)

#                 if 'actors' in row and not pd.isna(row['actors']):
#                     for actor_name in row['actors'].split(','):
#                         actor, _ = Actor.objects.get_or_create(name=actor_name.strip())
#                         movie.actors.add(actor)

#                 if 'countries' in row and not pd.isna(row['countries']):
#                     for country_name in row['countries'].split(','):
#                         country, _ = Country.objects.get_or_create(name=country_name.strip())
#                         movie.countries.add(country)

#                 if 'production_companies' in row and not pd.isna(row['production_companies']):
#                     for company_name in row['production_companies'].split(','):
#                         company, _ = ProductionCompany.objects.get_or_create(name=company_name.strip())
#                         movie.production_companies.add(company)
               
#                 if 'poster_url' in row and not pd.isna(row['poster_url']):
#                       movie.poster_url = row['poster_url']


#                 movie.save()

#             self.stdout.write(self.style.SUCCESS(f"Successfully imported data from {file_path}"))
#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"Error importing data: {e}"))
import pandas as pd
from django.core.management.base import BaseCommand
from films.models import Movie, Category, Director, Screenwriter, Actor, Country, ProductionCompany

class Command(BaseCommand):
    help = "Import movies from an Excel file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the Excel file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Read the Excel file
            data = pd.read_excel(file_path)

            for _, row in data.iterrows():
                # Create or update the Movie instance
                movie, created = Movie.objects.get_or_create(
                    original_title=row['original_title'],
                    defaults={
                        'title': row.get('title', ''),
                        'imdb_score': row.get('imdb_score', 0.0),
                        'release_year': row.get('release_year', 2000),
                        'description': row.get('description', 'No description available'),
                        'iframe_url': row.get('iframe_url', '<iframe></iframe>'),
                        'duration': row.get('duration', 0),
                    }
                )

                # Many-to-many relationships
                if 'categories' in row and not pd.isna(row['categories']):
                    for category_name in row['categories'].split(','):
                        category, _ = Category.objects.get_or_create(name=category_name.strip())
                        movie.categories.add(category)

                if 'directors' in row and not pd.isna(row['directors']):
                    for director_name in row['directors'].split(','):
                        director, _ = Director.objects.get_or_create(name=director_name.strip())
                        movie.directors.add(director)

                if 'screenwriters' in row and not pd.isna(row['screenwriters']):
                    for screenwriter_name in row['screenwriters'].split(','):
                        screenwriter, _ = Screenwriter.objects.get_or_create(name=screenwriter_name.strip())
                        movie.screenwriters.add(screenwriter)

                if 'actors' in row and not pd.isna(row['actors']):
                    for actor_name in row['actors'].split(','):
                        actor, _ = Actor.objects.get_or_create(name=actor_name.strip())
                        movie.actors.add(actor)

                if 'countries' in row and not pd.isna(row['countries']):
                    for country_name in row['countries'].split(','):
                        country, _ = Country.objects.get_or_create(name=country_name.strip())
                        movie.countries.add(country)

                if 'production_companies' in row and not pd.isna(row['production_companies']):
                    for company_name in row['production_companies'].split(','):
                        company, _ = ProductionCompany.objects.get_or_create(name=company_name.strip())
                        movie.production_companies.add(company)

                # Set poster_url if provided
                if 'poster_url' in row and not pd.isna(row['poster_url']):
                    movie.poster_url = row['poster_url']

                movie.save()

            self.stdout.write(self.style.SUCCESS(f"Successfully imported data from {file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing data: {e}"))
